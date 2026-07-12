# Conformance Claims

Conformance is evidence, not permission from CommonPact maintainers.

## Claim levels

1. **Core parser** — parses the strict envelope and reproduces event IDs.
2. **Core validator** — verifies proofs, payload schemas, extensions, error codes, and lifecycle semantics.
3. **Profile implementation** — passes a profile manifest, schemas, vectors, and complete transcript.
4. **Transport implementation** — passes a named transport profile and compatibility matrix.
5. **Portable client** — exports and imports complete pact packages independently.
6. **Operational deployment** — separately discloses operator, jurisdiction, support, optional providers, fees, legal review, safety and incident boundaries.

## Required report

A conformance report must identify software version, commit, language, dependencies, supported algorithms, core and profile versions, test-vector results, known deviations, unsupported critical extensions, transport matrix, and export/import evidence.

No implementation may use “certified,” “safe,” “official,” or “production-ready” merely because it passes repository vectors. No certification program exists today.
