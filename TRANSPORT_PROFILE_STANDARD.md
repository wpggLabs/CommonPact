# Transport Profile Standard

CommonPact semantics are transport-independent, but interoperability requires precise carrier profiles.

A transport profile MUST define:

- addressing and recipient discovery;
- public and private event carriage;
- encryption and sender-copy behavior;
- acknowledgements and their limited meaning;
- retry, deduplication, reordering, and expiry;
- relay or server authentication;
- capability negotiation and unsupported-version behavior;
- metadata exposure and privacy limitations;
- outage, migration, and provider-switching behavior;
- test fixtures and a client/provider compatibility matrix.

Nearby networking may support handoff verification or degraded operation. It MUST NOT be described as reliable wide-area discovery without measured evidence.
