# Prior Art

CommonPact combines existing ideas. It does not claim invention of federation, decentralized identity, signed events, encrypted messaging, credentials, open commerce, or peer-to-peer marketplaces.

Each entry records a lesson and a mismatch rather than using prior art as marketing validation.

## Email standards

**Lesson:** independent providers can interoperate below competing interfaces.  
**Mismatch:** email also demonstrates spam, metadata leakage, deliverability gatekeepers, and provider concentration. CommonPact needs explicit agreement, lifecycle, and evidence rather than unstructured messages.

## ActivityPub

Primary source: https://www.w3.org/TR/activitypub/

**Lesson:** a shared activity vocabulary can support federated servers and independent applications.  
**Mismatch:** social activities do not define canonical multi-party terms, exact signer sets, completion receipts, or domain responsibility.

## Matrix

Primary source: https://spec.matrix.org/

**Lesson:** open federation, room state, encryption, and multiple clients can coexist.  
**Mismatch:** a conversation room is not a domain agreement, physical handoff, or portable completion proof.

## Nostr

Primary source: https://github.com/nostr-protocol/nips

**Lesson:** signed events can move through replaceable relays without one canonical server.  
**Mismatch:** relay transport alone does not define agreement semantics, profile safeguards, or operational responsibility.

## W3C DIDs and Verifiable Credentials

Sources: https://www.w3.org/TR/did-core/ and https://www.w3.org/TR/vc-data-model-2.0/

**Lesson:** identifiers, verification methods, issuers, subjects, and portable claims can be separated.  
**Mismatch:** credentials do not negotiate terms or prove physical performance.

## Solid

Source: https://solidproject.org/TR/protocol

**Lesson:** user-controlled data and interoperable applications are viable architectural goals.  
**Mismatch:** portable storage does not itself define bilateral authorization, lifecycle, or evidence.

## Beckn Protocol

Source: https://developers.becknprotocol.io/

**Lesson:** open discovery and transaction protocols can span mobility, delivery, and commerce using domain schemas.  
**Mismatch:** CommonPact emphasizes user-held authorization, portable signed evidence, transport replaceability, and a strict claim-versus-receipt distinction. CommonPact should study Beckn's schema governance and network-operator experience rather than duplicate it.

## ONDC

Source: https://www.ondc.org/

**Lesson:** a public digital-commerce network can separate buyers, sellers, logistics, and network participants.  
**Mismatch:** ONDC is an operating regulated ecosystem with institutional governance and country-specific requirements; CommonPact is currently only a research RFC and must not imply equivalent deployment maturity.

## OpenBazaar

Source: https://github.com/OpenBazaar

**Lesson:** peer-to-peer marketplace discovery, direct trade, and optional moderation can reduce platform custody.  
**Mismatch:** operational history shows the difficulty of liquidity, moderation, dispute handling, incentives, maintenance, and user experience. CommonPact must not assume protocol openness automatically creates a sustainable market.

## PactRide

Repository: https://github.com/wpggLabs/PactRide

**Lesson:** a detailed domain proposal exposes privacy, lifecycle, safety, and responsibility constraints hidden by generic marketplace language.  
**Mismatch:** ride-specific concepts cannot become generic until they also work in a substantially different profile.
