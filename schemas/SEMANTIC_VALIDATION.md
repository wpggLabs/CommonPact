# Semantic Validation

JSON Schema is necessary but insufficient. Implementations must follow the deterministic order and stable error codes in `PROTOCOL.md`.

## Signer rules

- Every event requires at least one valid proof by `actor` unless a profile explicitly defines a multi-signature envelope event.
- Duplicate signers are invalid.
- Bilateral or multi-party events require the exact signer set declared by the profile and accepted terms.
- Revoked, expired, or out-of-scope delegated methods are invalid.

## Proposal and acceptance

- proposals and counters contain complete terms;
- `terms_hash` is recomputed from the canonical terms object;
- acceptance references one proposal and the identical hash;
- acceptance occurs before proposal expiry;
- all required roles authorize the same proposal, profile version, and role assignment.

## Causality and lifecycle

Direct predecessors must be available or the event remains pending. Stale, impossible, or replayed transitions are rejected. Competing valid branches are preserved and reported as conflict rather than resolved by arrival order.

## Extensions

Every critical extension must appear in `extensions` and be supported. Unknown noncritical values are retained where possible.

## Test-vector context

The fixture files include context such as expected signers, revoked signers, proposal expiry, expected terms hash, known predecessors, and allowed states. Context represents information an implementation would obtain from earlier accepted events and profile rules.
