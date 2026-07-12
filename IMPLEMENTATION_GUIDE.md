# Implementer Guide

Build a command-line implementation before a marketplace UI.

Minimum path:

1. parse the common envelope;
2. implement RFC 8785 canonicalization;
3. calculate event IDs;
4. verify proofs;
5. validate schemas;
6. apply signer and lifecycle rules;
7. exchange events through a local transport;
8. export a receipt;
9. import it in an independent implementation.

Do not begin with a global marketplace, real payments, public-road transportation, financial custody, a token, universal reputation, or a multi-profile super-app.

A useful first demonstration uses a fictional low-value PactRental asset with no money: publish availability, propose a period, accept identical terms, sign a handoff proof, sign a return receipt, and verify it across two clients.

Clients should show profile versions, unsupported extensions, fees, relay and optional-service dependencies, local trust policy, limits of signatures, and export/recovery behavior.
