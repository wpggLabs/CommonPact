# PactRental Research RFC Profile

**Identifier:** `pact-rental`  
**Version:** `0.1`  
**Status:** complete founder-authored Research RFC package; not independently implemented or operational  
**Maintainer:** `wpggLabs`

## Purpose

PactRental tests whether CommonPact can coordinate temporary possession or use of an asset without carrying ride-specific assumptions into the core.

## Non-goals

PactRental does not prove ownership, inspect an asset, hold a deposit, issue insurance, determine liability, authorize regulated rental activity, recover property, enforce payment, or replace courts and consumer-protection authorities.

## Parties and authority

- **Owner** — asserts control or authority to offer the asset.
- **Renter** — receives temporary possession or use.
- Optional **custodian** — performs handoff or storage.
- Optional **inspector** — provides condition evidence.
- Optional **guarantor**, **payment processor**, **escrow provider**, or **insurer**.

Owner and renter are required agreement signers. A custodian may be required for activation or return when canonical terms specify that role. External providers do not become agreement parties unless explicitly assigned a role.

## Discovery

Public intent may include asset category, broad availability, approximate area, capacity or compatibility, broad price range, and required credential classes.

Public discovery MUST NOT include exact storage address, access codes, serial numbers, identity documents, security systems, precise recurring schedule, full ownership documents, or unredacted condition evidence.

Intent lifetime MUST be positive and SHOULD be short enough to limit routine correlation.

## Private negotiation

Private fields may include exact asset reference, handoff and return location, detailed condition, credentials, insurance, payment provider, deposit method, permitted use, geography, mileage, maintenance, fuel, cancellation, refunds, late return, damage evidence, and support contacts.

## Canonical agreement terms

The terms object MUST include:

- owner and renter identities and roles;
- asset reference and disclosed baseline condition;
- start, end, grace period, and return deadline;
- handoff and return procedure;
- price, currency, external payment reference, and settlement state vocabulary;
- deposit or escrow provider and release conditions, if any;
- permitted and prohibited use;
- geographic, mileage, capacity, and operator limits;
- maintenance, charging, fuel, cleaning, and storage obligations;
- required credentials, insurance, or guarantor;
- cancellation, no-show, late return, early termination, and refund rules;
- condition evidence method and retention period;
- dispute and external-resolution references;
- accessibility commitments;
- agreement-affecting extensions.

## Acceptance

Owner and renter MUST each authorize the same proposal event, terms hash, role assignment, and profile version before expiry. A custodian does not substitute for either party. Stale, crossed, or partially patched terms do not create a reservation.

## Lifecycle

See `LIFECYCLE.md`. The main path is:

`Available → Negotiating → Reserved → HandedOver → InUse → ReturnClaimed → Returned`

Terminal or conflict outcomes include `Withdrawn`, `Expired`, `Declined`, `Cancelled`, `Aborted`, `Overdue`, `RecoveryClaimed`, `Disputed`, and `ResolvedExternally`.

## Activation and handoff proof

Handoff proof requires owner and renter, plus a custodian when required by terms. It binds accepted terms, asset reference, time, handoff location class, odometer or usage baseline where applicable, condition evidence hashes, provided accessories, and disclosed exceptions.

The proof does not prove hidden condition, legal ownership, mechanical safety, or that the evidence is complete.

## Progress and changes

Permitted updates may include voluntary extension proposal, maintenance notice, authorized operator change, temporary storage, usage checkpoint, or support incident. Agreement-affecting changes require a new complete terms object and required acceptance.

## Cancellation and abnormal termination

Before handoff, the profile uses cancellation. After handoff, early termination uses abort or profile-specific recovery events. An owner cannot unilaterally mark an asset returned; a renter cannot unilaterally convert a return claim into a bilateral receipt.

## Completion and receipt

A return claim records one party's statement. A return receipt requires the exact signer set defined by the terms, normally owner and renter. It binds accepted terms, handoff proof, return time, condition declaration, usage summary, returned accessories, settlement declaration, and evidence hashes.

A return receipt does not prove no latent damage exists or that payment and deposit settlement are irreversible.

## Disputes

Competing condition, possession, usage, payment, or timing evidence is preserved. External inspector, insurer, escrow, arbitrator, court, or law-enforcement references may be attached without pretending CommonPact adjudicated the result.

## Ratings, attestations, warnings, and revocation

Ratings SHOULD reference a completed or disputed pact. Ownership, credentials, insurance, inspection, and custodian authority remain separately attributable attestations. Warnings must preserve issuer, scope, evidence references, and revocation status.

## Privacy, accessibility, abuse, and safety

See `PRIVACY_ACCESSIBILITY_AND_ABUSE.md`.

## Payments and settlement

PactRental records only method-neutral declarations and external references. It does not hold deposits, guarantee escrow, initiate chargebacks, or determine final settlement.

## Failure and migration

Clients must handle duplicate and reordered events, stale acceptance, unavailable evidence, lost keys, unsupported extensions, provider outage, and partial export. Major profile changes require explicit migration; old events are not silently reinterpreted.

## Artifacts

- `profile-manifest.json`
- `LIFECYCLE.md`
- `TERMS_AND_EVIDENCE.md`
- `PRIVACY_ACCESSIBILITY_AND_ABUSE.md`
- `RESPONSIBILITY_BOUNDARIES.md`
- `schemas/pactrental-profile.schema.json`
- `test-vectors/pactrental-v0.1.json`
- `../../examples/pact-rental-transcript.md`

## Status boundary

This package completes the founder-authored abstraction test. It is not independent evidence that CommonPact or PactRental works.
