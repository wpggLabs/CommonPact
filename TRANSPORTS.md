# Transports

CommonPact events should retain meaning whether delivered through federated or Nostr-compatible relays, HTTPS or WebSocket services, direct encrypted channels, institutional servers, local networks, Bluetooth or nearby exchange, or store-and-forward bundles.

## Practical baseline

1. Publish discovery intent to multiple replaceable internet relays.
2. Discover and match in clients.
3. Negotiate over encrypted private messaging.
4. Store encrypted local event history.
5. Use direct or nearby exchange for verification and resilience.

## Mesh limitation

Phone-to-phone mesh is not assumed to provide dependable citywide discovery. Mobile systems restrict background execution, advertising, scanning, and peer connectivity. Multi-hop mesh remains research until measured.

## Delivery is not agreement

A relay acknowledgement proves transport handling only. It does not prove agreement, activation, completion, payment, or physical performance.

## Carrier requirements

A carrier profile documents addressing, encryption, duplicates, ordering, expiration, retry, acknowledgements, sender copies, relay discovery, outage behavior, metadata leakage, capability negotiation, and migration.
