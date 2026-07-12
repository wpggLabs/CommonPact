# Interoperability

CommonPact is interoperable only when independently written implementations interpret the same events and lifecycle consistently.

## Minimum evidence

A conformance claim requires deterministic canonicalization and event IDs, proof verification, schema and semantic validation, lifecycle validation, duplicate and reordering behavior, unsupported-version handling, and portable evidence export/import.

## Independent implementation

The repository validator is a development aid, not proof. At least two implementations in different languages should generate the same event ID, verify the same proof, reject the same invalid fixtures, complete the same transcript, and import the same receipt.

## Possible conformance levels

- **Core parser** — envelope and event-ID support.
- **Core validator** — schemas, proofs, and lifecycle checks.
- **Profile compatible** — passes one profile's vectors.
- **Transport compatible** — passes a named carrier matrix.
- **Product claim** — also discloses policy, optional services, and unsupported features.

No certification program exists today.
