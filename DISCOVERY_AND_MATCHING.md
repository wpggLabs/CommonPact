# Discovery and Matching

Discovery lets counterparties find relevant intents without publishing the full pact.

## Public intent

A public intent should be signed, short-lived, profile-qualified, minimally descriptive, privacy-reviewed, and independently validatable.

Profiles divide information into safe public discovery fields, encrypted negotiation fields, post-agreement disclosure, local-only data, and prohibited data.

Examples:

- PactRide may publish a coarse zone but not an exact home address.
- PactRental may publish an asset category but not a private storage location.
- PactDelivery may publish a route corridor but not a recipient address.
- PactFund may publish campaign purpose while restricting beneficiary records.

## Relays and matching

Relays distribute events; they do not become the canonical dispatcher. Clients may subscribe to several relays, match locally, use community indexes, apply visible ranking policy, and reject events under local trust or jurisdiction rules.

## Ranking transparency

A client should disclose material factors such as fees, sponsorship, distance, availability, trust evidence, policy, compatibility, and accessibility. The core does not prescribe a global ranking algorithm.

## Spam controls

Possible controls include expiration, rate limits, relay authentication, block lists, profile-specific deposits or attestations, and optional proof-of-work. None should be presented as a universal identity or trust solution.
