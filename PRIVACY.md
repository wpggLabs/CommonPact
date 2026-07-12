# Privacy

## Threat model

Coordination data can reveal:

- identity;
- location;
- routines;
- social relationships;
- asset ownership;
- financial need;
- health or accessibility requirements;
- donation recipients;
- commercial activity.

## Data classes

Profiles must classify fields as:

- public discovery;
- encrypted negotiation;
- post-agreement disclosure;
- local-only;
- prohibited.

## Core privacy rules

- Public intents use expiration.
- Exact sensitive details do not appear in public discovery unless a profile justifies them.
- Relays receive only necessary metadata.
- Long-term identity should not be exposed before needed.
- Clients should avoid continuous public status.
- Evidence exports should support minimization.
- Deletion claims must account for copies held by counterparties and relays.

## Metadata limits

Encryption does not hide all metadata. Timing, relay choice, message size, IP address, repeated identifiers, and social graphs may remain visible.

## Profile examples

- Ride: coarse origin zone publicly, exact pickup privately.
- Rental: asset class publicly, storage address after agreement.
- Delivery: route corridor publicly, recipient address privately.
- Fund: campaign purpose publicly, sensitive beneficiary records restricted.

## No anonymity promise

CommonPact may support pseudonymous or privacy-preserving use, but profiles may require verified identity or regulated records. The project must not promise anonymous high-risk transactions without accountability.

## Related controls

See [`DATA_PORTABILITY.md`](DATA_PORTABILITY.md), [`ABUSE_AND_MODERATION.md`](ABUSE_AND_MODERATION.md), and [`ACCESSIBILITY.md`](ACCESSIBILITY.md). Portability does not mean public disclosure, and deletion cannot recall copies already held by counterparties or infrastructure.
