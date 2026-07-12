#!/usr/bin/env python3
"""Validate CommonPact schemas, Ed25519 fixtures, and PactRental artifacts."""
import base64, copy, hashlib, json, sys
from datetime import datetime
from pathlib import Path
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def canonical(value):
    # Fixtures use no floats; this is byte-identical to RFC 8785 for their JSON types.
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def signing_object(event):
    value = copy.deepcopy(event)
    value.pop("event_id", None)
    value.pop("proofs", None)
    return value


def event_id(event):
    return "sha256:" + hashlib.sha256(canonical(signing_object(event))).hexdigest()


def b58decode(text):
    number = 0
    for char in text:
        number = number * 58 + B58.index(char)
    raw = number.to_bytes((number.bit_length() + 7) // 8, "big") if number else b""
    return b"\0" * (len(text) - len(text.lstrip("1"))) + raw


def public_key(did):
    if not did.startswith("did:key:z"):
        raise ValueError("unsupported verification method")
    raw = b58decode(did[9:])
    if len(raw) != 34 or raw[:2] != b"\xed\x01":
        raise ValueError("invalid Ed25519 did:key")
    return Ed25519PublicKey.from_public_bytes(raw[2:])


def time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def schema_error(validator, value):
    errors = sorted(validator.iter_errors(value), key=lambda error: list(error.path))
    return errors[0] if errors else None


def materialize(case):
    event = load("test-vectors/" + case["fixture"])
    mutation = case.get("mutation")
    if mutation == "wrong_protocol":
        event["protocol"] = "other"
    elif mutation == "event_id_mismatch":
        event["event_id"] = "sha256:" + "f" * 64
    elif mutation == "invalid_signature":
        event["proofs"][0]["signature"] = "AAAA"
    elif mutation == "duplicate_signer":
        event["proofs"].append(dict(event["proofs"][0]))
    elif mutation == "unexpected_signer":
        signer = "did:key:z6MkqUpi2KAV8eRKRD9XHb6Td83RwP9ULKoZWSWa31ypD8Pf"
        event["proofs"][1]["signer"] = signer
        event["proofs"][1]["verification_method"] = signer + "#key-1"
    elif mutation == "unknown_critical_extension":
        key = "example.org/required-policy"
        event["extensions"][key] = {"mode": "strict"}
        event["critical_extensions"] = [key]
    elif mutation:
        raise ValueError(f"unknown mutation: {mutation}")
    return event


def validate(event, context, envelope, event_validators):
    if schema_error(envelope, event):
        return "CP-ENV-001"
    validator = next((v for types, v in event_validators if event["event_type"] in types), None)
    if validator is None or schema_error(validator, event):
        return "CP-PAY-001"
    if context.get("minimum_profile_version") and event["profile_version"] < context["minimum_profile_version"]:
        return "CP-VER-002"
    supported = set(context.get("supported_critical_extensions", []))
    if any(key not in event["extensions"] or key not in supported for key in event["critical_extensions"]):
        return "CP-EXT-001"
    if event_id(event) != event["event_id"]:
        return "CP-ID-001"
    signers = [proof["signer"] for proof in event["proofs"]]
    if len(signers) != len(set(signers)):
        return "CP-PROOF-003"
    expected = context.get("expected_signers")
    if expected is not None and set(signers) != set(expected):
        return "CP-PROOF-003"
    if event["actor"] not in signers:
        return "CP-PROOF-002"
    if set(context.get("revoked_signers", [])).intersection(signers):
        return "CP-PROOF-004"
    message = canonical(signing_object(event))
    for proof in event["proofs"]:
        try:
            encoded = proof["signature"] + "=" * (-len(proof["signature"]) % 4)
            public_key(proof["signer"]).verify(base64.urlsafe_b64decode(encoded), message)
        except (ValueError, InvalidSignature):
            return "CP-PROOF-001"
    if "expires_at" in event and time(event["expires_at"]) <= time(event["created_at"]):
        return "CP-TIME-001"
    if context.get("proposal_expires_at") and time(event["created_at"]) > time(context["proposal_expires_at"]):
        return "CP-TIME-001"
    if "known_previous" in context and not set(event["previous"]).issubset(context["known_previous"]):
        return "CP-CAUSE-001"
    if event["event_type"] in {"pact.proposal", "pact.counter"}:
        computed = "sha256:" + hashlib.sha256(canonical(event["payload"]["terms"])).hexdigest()
        if computed != event["payload"]["terms_hash"]:
            return "CP-TERMS-001"
    if context.get("expected_terms_hash") and event.get("payload", {}).get("terms_hash") != context["expected_terms_hash"]:
        return "CP-TERMS-001"
    if context.get("allowed_event_types") and event["event_type"] not in context["allowed_event_types"]:
        return "CP-STATE-001"
    return None


def main():
    checker = FormatChecker()
    envelope = Draft202012Validator(load("schemas/commonpact-envelope.schema.json"), format_checker=checker)
    groups = [
        ({"intent.publish", "intent.withdraw", "pact.proposal", "pact.counter", "pact.decline", "pact.accept"}, "schemas/events/discovery-negotiation.schema.json"),
        ({"pact.activate", "pact.update", "pact.cancel", "pact.abort", "pact.completion.claim", "pact.completion.receipt", "pact.dispute", "pact.resolution.reference"}, "schemas/events/lifecycle.schema.json"),
        ({"evidence.attestation", "evidence.revocation", "moderation.warning", "identity.binding", "capability.declaration"}, "schemas/events/evidence-capability.schema.json"),
    ]
    event_validators = [(types, Draft202012Validator(load(path), format_checker=checker)) for types, path in groups]
    manifest_validator = Draft202012Validator(load("schemas/profile-manifest.schema.json"), format_checker=checker)
    rental_validator = Draft202012Validator(load("profiles/pactrental/schemas/pactrental-profile.schema.json"), format_checker=checker)
    vectors = load("test-vectors/core-v0.1.json")
    failures = []
    for case in vectors["cases"]:
        error = validate(materialize(case), case.get("context", {}), envelope, event_validators)
        if case["valid"] and error:
            failures.append(f"{case['name']}: expected valid, got {error}")
        elif not case["valid"] and error != case["expected_error"]:
            failures.append(f"{case['name']}: expected {case['expected_error']}, got {error}")
    manifest_error = schema_error(manifest_validator, load("profiles/pactrental/profile-manifest.json"))
    if manifest_error:
        failures.append(f"PactRental manifest: {manifest_error.message}")
    rental_cases = load("profiles/pactrental/test-vectors/pactrental-v0.1.json")["cases"]
    for case in rental_cases:
        valid = schema_error(rental_validator, case["data"]) is None
        if valid != case["valid"]:
            failures.append(f"{case['name']}: expected valid={case['valid']}, got {valid}")
    if len(load("examples/minimal-pact.json").get("events", [])) < 7:
        failures.append("minimal transcript must contain the full seven-event path")
    if failures:
        print("Protocol validation failed:")
        print("\n".join("- " + failure for failure in failures))
        return 1
    print(f"Validated {len(vectors['cases'])} core cases, {len(rental_cases)} PactRental cases, manifest, and transcript.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
