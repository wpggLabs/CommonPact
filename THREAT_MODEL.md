# Threat Model

Adversaries include discovery spammers, stalkers correlating routines, malicious counterparties, colluding reputation farms, compromised relays, metadata observers, stolen keys, malicious clients, dishonest attestors, payment or escrow fraud, operators hiding responsibility, and governance capture.

| Threat | Initial control | Remaining risk |
|---|---|---|
| Event forgery | signatures and event IDs | key compromise |
| Replay | expiration, causality, idempotency | delayed valid events |
| Terms substitution | complete terms and hash | deceptive UI |
| False completion | claim/receipt distinction | colluding signers |
| Evidence erasure | conflict preservation/export | inaccessible copies |
| Public leakage | profile minimization | metadata correlation |
| Relay capture | multi-relay support | dominant providers |
| Sybil identities | local policy/attestations | privacy tradeoffs |
| Malicious extension | namespacing/critical flag | implementation bugs |
| Governance capture | public RFCs/forkability | social concentration |

Cryptography cannot prove a ride was safe, an asset was undamaged, a package contained what was claimed, campaign funds were used honestly, a participant had legal authority, or a payment is irreversible.
