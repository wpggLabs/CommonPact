# CommonPact Profile Standard

A profile defines one domain's meaning on top of the CommonPact core. A profile is not merely a list of custom fields; it is a complete contract for roles, lifecycle, proof, privacy, responsibility, and interoperability.

## Required profile package

Every profile seeking **Research RFC** status MUST include:

1. identifier, semantic version, status, maintainers, and repository;
2. purpose, use cases, and explicit non-goals;
3. parties, roles, authority, delegation, and required signer matrix;
4. public discovery schema and maximum lifetime;
5. data prohibited from public discovery;
6. private negotiation fields and disclosure timing;
7. canonical agreement terms and hashing input;
8. proposal, counter, decline, and acceptance semantics;
9. aggregate and thread lifecycle state machines;
10. activation, handoff, or start proof;
11. progress events and permitted authors;
12. cancellation and abnormal termination rules;
13. completion claims and exact receipt signer set;
14. disputes, conflicting evidence, and external resolution references;
15. ratings, attestations, warnings, and revocations;
16. privacy, metadata, abuse, and coercion risks;
17. accessibility requirements and prohibited inaccessible defaults;
18. safety, legal, insurance, tax, licensing, and operational responsibility;
19. payment, escrow, refund, chargeback, or settlement references;
20. failure, retry, replay, migration, and older-client behavior;
21. strict schemas and semantic validation rules;
22. valid and invalid conformance vectors;
23. at least one complete fictional transcript;
24. a mapping showing which concepts remain profile-specific.

## Profile manifest

Every profile MUST publish a machine-readable manifest conforming to `schemas/profile-manifest.schema.json`. Registration is informational; it is not permission, certification, endorsement, or proof of safety.

## Strictness rule

A profile MAY be stricter than the CommonPact core. It MUST NOT weaken:

- canonicalization and event-ID rules;
- proof binding and signer uniqueness;
- provenance and causal references;
- conflict preservation;
- critical-extension handling;
- version negotiation;
- claims-versus-receipts distinction;
- data-minimization requirements declared by the profile itself.

## Abstraction rule

A feature MUST NOT become core merely because one profile needs it. Before extraction it SHOULD:

1. work naturally in at least two substantially different profiles;
2. avoid domain terminology and hidden assumptions;
3. preserve stricter profile safeguards;
4. have documented privacy and security consequences in both domains;
5. have compatible schemas, vectors, and migration behavior;
6. be accepted through both projects' public governance.

## Status labels

- **Concept** — problem, actors, and boundaries only.
- **Draft** — coherent terms and lifecycle; artifacts incomplete.
- **Research RFC** — complete founder-authored profile package, schemas, vectors, and transcript.
- **Interoperability candidate** — independent implementations are testing the profile.
- **Proven profile** — published evidence satisfies the profile's conformance gates.
- **Operational deployment** — one accountable deployment exists; this is not universal safety or legality.

## Required review questions

Reviewers SHOULD ask:

- Does the profile hide a domain-specific obligation inside a generic field?
- Can a malicious client make a user authorize different terms than displayed?
- Which data becomes public, linkable, or permanent?
- Who is responsible when the protocol evidence is insufficient?
- Does the profile assume one payment, identity, moderation, or transport provider?
- Can users export evidence and move to another compatible client?
- What does the profile explicitly refuse to solve?
