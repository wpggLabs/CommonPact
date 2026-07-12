# Evidence and Receipts

CommonPact preserves statements with provenance instead of converting every signal into one global truth score.

Evidence may include pact events, receipts, identity or credential attestations, condition evidence, custody handoff proofs, payment references, warnings, revocations, and external resolution references.

## Claim versus receipt

A claim is one actor's signed statement. A receipt is an event authorized by the signer set required by the profile over one identical event body. It proves those keys authorized the record, not that every physical fact is true.

## Portable history

Users should be able to export accepted terms, lifecycle events, receipts, attestations, revocations, warnings, provenance, and verification metadata without a central history service.

## Selective disclosure

Presenting a whole historical pact may expose sensitive data. Implementations should support profile-defined minimization or redacted proofs without inventing unverifiable summaries.

## Conflicting evidence

If valid events conflict, clients preserve both and surface a disputed state. Relay order, popularity, or one application's database must not erase competing evidence.

## Ratings

Profiles define who may rate, which completed or aborted pact is referenced, allowed dimensions, privacy limits, abuse handling, and whether the rating is public, private, or selectively disclosed.
