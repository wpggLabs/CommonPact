# Negotiation and Agreement

Exact terms and sensitive details should be exchanged through encrypted channels when possible.

## Proposal threads

Each counterparty negotiation is independent. A profile may define a thread identifier to prevent crossed messages.

## Complete proposal rule

Every proposal and counterproposal contains complete proposed terms. A client must not create agreement by applying ambiguous partial changes to an older proposal.

Terms should state parties and roles, subject, obligations, timing, consideration, cancellation and refund conditions, required commitments, optional-service dependencies, and all extensions affecting agreement.

## Acceptance

Acceptance references one proposal and one terms hash. Agreement requires all profile-required authorizations over the same canonical input. A message delivery receipt, button click without protocol authorization, or unilateral database update is not sufficient.

## Invalid agreement conditions

Clients reject or surface acceptance of an expired proposal, acceptance after an incompatible counter, mismatched terms hashes, wrong roles, unexpected signers, and acceptance from another thread.

## External contracts

A CommonPact agreement may reference legal contracts, waivers, invoices, escrow terms, or disclosures. The protocol does not decide legal enforceability.
