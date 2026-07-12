# Responsibility Boundaries

| Concern | Core | Profile | Client/operator | External provider |
|---|---|---|---|---|
| Event envelope | Defines | Uses | Implements | — |
| Domain roles | Extension point | Defines | Presents/enforces | May attest |
| Discovery privacy | Baseline minimization | Defines fields | Configures and warns | Relay handles metadata |
| Matching | No global algorithm | May define constraints | Performs and ranks | Index may assist |
| Agreement | Canonical mechanism | Defines terms/signers | Obtains authorization | Legal service may review |
| Physical performance | Does not prove | Defines evidence model | Supports workflow | Operator performs/supports |
| Payment | References only | Defines settlement fields | Integrates and discloses | Processor/escrow settles |
| Insurance | No coverage | Defines requirements | Blocks unsupported use | Insurer provides coverage |
| Identity verification | Proof plumbing | Defines required credentials | Selects policy | Verifier issues attestation |
| Moderation | Evidence format | Defines domain warnings | Applies local policy | Community/service may moderate |
| Disputes | Preserves evidence | Defines dispute events | Supports users | Court/arbitrator/service resolves |
| Emergency response | None | Documents boundaries | Provides operational plan | Emergency services respond |
| Legal compliance | None | Documents known concerns | Determines availability | Counsel/regulators advise |
| Accessibility | Generic extension support | Defines needs | Implements accessible UX | Specialists review |

## Rule

A protocol feature must not be used to imply that an unassigned operational responsibility has disappeared.

## Deployment gate

Before a real pilot, apply [`LEGAL_REVIEW_CHECKLIST.md`](LEGAL_REVIEW_CHECKLIST.md) and name owners for accessibility, abuse response, payment or custody, insurance, privacy, support, incidents, and shutdown.
