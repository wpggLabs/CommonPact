# CommonPact Protocol Core

**Status:** draft v0.1 research baseline  
**Normative language:** MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are used in the RFC 2119 sense.

This document defines the domain-neutral CommonPact wire and validation model. Profiles add domain meaning and stricter requirements; they do not weaken the core.

## 1. Event envelope

Every event MUST use the strict envelope defined in `schemas/commonpact-envelope.schema.json`.

```json
{
  "protocol": "commonpact",
  "protocol_version": "0.1",
  "profile": "pact-rental",
  "profile_version": "0.1",
  "event_type": "pact.proposal",
  "event_id": "sha256:...",
  "pact_id": "urn:uuid:...",
  "thread_id": "urn:uuid:...",
  "actor": "did:key:...",
  "created_at": "2026-07-11T18:00:00Z",
  "expires_at": "2026-07-11T18:10:00Z",
  "previous": ["sha256:..."],
  "payload": {},
  "extensions": {},
  "critical_extensions": [],
  "proofs": []
}
```

### 1.1 Required invariants

An implementation MUST reject an event when any of the following is true:

1. `protocol` is not `commonpact`.
2. the core or profile version is unsupported for the requested operation;
3. the envelope or event payload fails its JSON Schema;
4. an identifier, timestamp, causal reference, proof, or extension is malformed;
5. the calculated event ID differs from `event_id`;
6. a required proof is missing, invalid, duplicated, revoked, expired, or unauthorized;
7. an unknown critical extension is present;
8. the event violates the profile lifecycle, signer matrix, or semantic rules.

## 2. Canonicalization and identifiers

The v0.1 signing object is the complete envelope with `event_id` and `proofs` omitted. It MUST be canonicalized using RFC 8785 JSON Canonicalization Scheme and hashed with SHA-256.

`event_id` MUST be formatted as `sha256:<64 lowercase hexadecimal characters>`.

Profiles MUST NOT redefine canonicalization, event IDs, proof binding, or extension criticality within the same CommonPact major version.

`pact_id` identifies one coordination aggregate. `thread_id` identifies one negotiation thread when several counterparties negotiate independently. Declining one thread MUST NOT silently withdraw the whole pact aggregate.

## 3. Proof model

Each proof contains:

- `signer` — the identity that authorizes the event;
- `verification_method` — the key or delegated method used;
- `algorithm` — a registered signature algorithm;
- `signature` — the encoded signature;
- optional `delegation` — the event or credential authorizing limited action.

The v0.1 interoperability fixtures use Ed25519. Other algorithms MAY be profiled only with deterministic encoding, verification rules, downgrade behavior, and test vectors.

A valid signature proves only that the corresponding key authorized the signing object. It does not prove legal identity, truth, physical performance, payment, safety, ownership, charitable status, or regulatory compliance.

### 3.1 Duplicate and unexpected signers

A proof set MUST contain no duplicate signer. A profile MUST define the expected signer set for bilateral or multi-party events. Extra signers MUST NOT silently satisfy the requirement.

### 3.2 Delegation

Delegation MUST bind the delegator, delegate, permitted profiles, permitted event families, scope, expiry, and revocation reference. An implementation MUST apply the narrower of the delegation and profile permissions.

## 4. Core event families

| Event | Purpose | Minimum authorization | Normal state effect |
|---|---|---|---|
| `intent.publish` | Publish an expiring, privacy-limited need or availability | actor | Creates discoverable intent |
| `intent.withdraw` | Stop an intent from being actionable | original actor or valid delegate | Withdrawn |
| `pact.proposal` | Offer complete canonical terms | proposer | Negotiating |
| `pact.counter` | Replace prior proposed terms with complete terms | counterparty | Negotiating |
| `pact.decline` | Reject one negotiation thread | declining party | Thread declined |
| `pact.accept` | Authorize one proposal and terms hash | one required party per event | Contributes to agreement |
| `pact.activate` | Record profile-defined activation or handoff | profile signer set | Active |
| `pact.update` | Record permitted lifecycle progress | profile-authorized actor | Profile-defined |
| `pact.cancel` | End before activation | profile signer rule | Cancelled |
| `pact.abort` | End abnormally after activation | profile signer rule | Aborted |
| `pact.completion.claim` | One party claims completion | claimant | Completion claimed |
| `pact.completion.receipt` | Required parties authorize identical completion evidence | exact profile signer set | Completed |
| `pact.dispute` | Preserve conflicting claims or evidence | disputing party | Disputed |
| `pact.resolution.reference` | Reference an external resolution without pretending the protocol adjudicated | profile-authorized actor or resolver | Resolved externally |
| `evidence.attestation` | Publish a scoped external claim | attestor | No automatic lifecycle change |
| `evidence.revocation` | Revoke a prior attestation, delegation, or key assertion | authorized issuer | Evidence invalidated prospectively |
| `moderation.warning` | Publish a scoped warning with provenance | warning issuer | Local-policy input only |
| `identity.binding` | Privately bind temporary and longer-term identities | both identities or authorized controller | Identity continuity |
| `capability.declaration` | Advertise supported core, profiles, transports, and extensions | declaring client or actor | Capability discovery |

The payload contract for every event is defined as a separate named schema in `schemas/pact-event-types.schema.json`.

## 5. Complete terms and agreement

A proposal or counter MUST carry the complete proposed agreement input, not a partial patch. The canonical terms object MUST include:

- profile identifier and version;
- party identities and role assignments;
- obligations and prohibited actions;
- timing, duration, expiry, or validity window;
- consideration and settlement declaration where relevant;
- profile-required accessibility, privacy, safety, and operational commitments;
- cancellation, abnormal termination, and dispute terms;
- all extensions marked as affecting agreement.

`terms_hash` MUST be the SHA-256 hash of the RFC 8785 canonical terms object.

Agreement exists only when the profile-required parties authorize the same `pact_id`, `thread_id`, proposal event, terms hash, profile version, and role assignment before the proposal expires.

Crossed messages, partial counters, stale acceptances, mismatched hashes, unsupported critical extensions, and unauthorized signers MUST NOT create agreement.

## 6. Lifecycle and causality

The generic lifecycle is defined in `PACT_LIFECYCLE.md`. Profiles MUST publish an explicit transition table and signer matrix.

`previous[]` MUST contain every direct causal predecessor required by the event semantics. Clients MUST:

- process duplicates idempotently;
- retain events received out of order until predecessors arrive or a documented timeout applies;
- reject impossible or stale transitions;
- preserve valid competing branches;
- avoid resolving conflict by transport arrival order;
- distinguish thread state from aggregate state.

A relay acknowledgement, push notification, read receipt, or message delivery result is never agreement or lifecycle proof.

## 7. Claims, evidence, and receipts

A completion claim is one actor's signed statement. A completion receipt is a different event requiring the exact signer set defined by the profile over one identical event.

Receipts MUST bind:

- accepted terms hash;
- activation or handoff proof reference;
- completion time or interval;
- profile-defined outcome and evidence hashes;
- limited settlement declaration;
- exact signer set.

A receipt MUST NOT claim more than it proves. External evidence MAY later contradict a receipt. Conflicting valid evidence MUST be retained and may produce a disputed state.

## 8. Expiration and replay

Public intent events MUST have a positive expiry. Profiles SHOULD set maximum lifetimes based on privacy and operational risk.

Expiration makes an event non-actionable; it does not erase the historical signed event. An implementation MUST reject replay when the event is expired, already consumed in an incompatible state, references stale terms, or violates a profile replay rule.

## 9. Extensions

Every extension key MUST be namespaced as `authority/name`.

`critical_extensions` is an array of extension keys whose semantics are required to interpret or authorize the event. If a critical extension is unknown or unsupported, the operation MUST fail with `CP-EXT-001` rather than being silently accepted.

Unknown noncritical extensions SHOULD be retained when forwarding or exporting even when ignored locally.

## 10. Version negotiation

- Patch releases clarify behavior without changing valid wire meaning.
- Minor releases may add compatible optional behavior.
- Major releases may change canonicalization, proof rules, lifecycle semantics, or required payloads.
- Profiles version independently from the core.
- A capability declaration SHOULD state supported core versions, profile versions, transports, algorithms, and extensions.
- A client MUST NOT silently downgrade an agreement-affecting feature.

## 11. Deterministic validation order

Implementations MUST validate in this order so independent implementations report the same primary failure:

1. parse JSON and reject duplicate object keys;
2. validate the strict envelope schema;
3. validate the event payload schema;
4. validate version and capability support;
5. validate extension names and critical support;
6. reconstruct the signing object and verify `event_id`;
7. validate proofs, delegation, revocation, and signer uniqueness;
8. validate identifiers, timestamps, expiry, and direct causal references;
9. validate profile signer matrix and canonical terms hash;
10. validate lifecycle transition and replay rules;
11. retain or export the accepted event.

## 12. Error codes

| Code | Meaning |
|---|---|
| `CP-JSON-001` | Invalid JSON or duplicate key |
| `CP-ENV-001` | Envelope schema failure |
| `CP-PAY-001` | Event payload schema failure |
| `CP-VER-001` | Unsupported core or profile version |
| `CP-VER-002` | Unsafe downgrade attempt |
| `CP-EXT-001` | Unknown critical extension |
| `CP-ID-001` | Event ID mismatch |
| `CP-PROOF-001` | Invalid signature |
| `CP-PROOF-002` | Missing required signer |
| `CP-PROOF-003` | Duplicate or unexpected signer |
| `CP-PROOF-004` | Revoked, expired, or unauthorized verification method |
| `CP-TIME-001` | Invalid timestamp or expiry |
| `CP-CAUSE-001` | Missing, stale, or malformed causal reference |
| `CP-TERMS-001` | Terms hash or proposal reference mismatch |
| `CP-STATE-001` | Invalid lifecycle transition |
| `CP-REPLAY-001` | Replay or already-consumed event |
| `CP-PROFILE-001` | Profile semantic rule failure |

Implementations MAY expose additional diagnostics, but conformance reports SHOULD preserve these stable primary codes.

## 13. Conflict handling

When two valid events cannot both be true under one profile state, clients MUST retain both branches, mark the pact disputed or unresolved, and make provenance inspectable. The core does not choose the morally correct party or enforce external remedies.

## 14. Security boundary

The protocol authenticates statements and relationships between statements. It does not authenticate the physical world. Profiles and deployments remain responsible for domain safety, law, accessibility, payment, insurance, incident response, and human support.
