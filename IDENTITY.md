# Identity and Authorization

## User-controlled keys

CommonPact identities are authorized through cryptographic keys controlled by participants or their delegated clients.

## Identity is layered

The protocol distinguishes:

- a key or identifier;
- proof that a key authorized an event;
- continuity between temporary and long-term identifiers;
- attestations made by external entities;
- legal identity or credential status;
- local trust decisions.

These are not interchangeable.

## Discovery privacy

Profiles may permit rotating discovery identities. Before long-term identity is relied upon for agreement, a private proof-backed binding should connect the discovery identity to the accepting identity.

## Delegation

A participant may delegate limited authority to a device, organization, guardian, employee, fleet, courier, or automated agent. Delegation must state scope, expiry, revocation, and profile applicability.

## Recovery and rotation

Profiles and clients must account for:

- lost keys;
- compromised keys;
- key rotation;
- revocation;
- multi-device use;
- historical proof verification.

No recovery service is mandatory at the protocol level.

## No universal verification

CommonPact does not create one "verified person" status. A client may require government identity, organization credentials, licenses, background checks, community attestations, or no external verification depending on profile, jurisdiction, and risk.

## Detailed recovery rules

See [`KEY_MANAGEMENT_AND_RECOVERY.md`](KEY_MANAGEMENT_AND_RECOVERY.md) for device keys, delegation, social or provider recovery, rotation, compromise, and historical continuity.
