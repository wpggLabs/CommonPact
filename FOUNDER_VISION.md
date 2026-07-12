# CommonPact Founder Vision and Documentation Completion

**Founder-vision status:** complete as of 2026-07-11  
**Project maturity:** pre-implementation research RFC  
**Canonical implementation status:** [`STATUS.md`](STATUS.md)

## Origin

The original idea began with PactRide.

Today, when a person wants a ride, they normally open an application controlled by a company such as Uber or Lyft. That company operates the discovery and matching infrastructure, controls access to riders and drivers, sets or influences pricing, owns the reputation system, retains transaction records, and charges fees because every interaction must pass through its platform.

The founder's question was not simply how to create another rideshare company. It was:

**Can riders and drivers coordinate directly through an open protocol, the way people can exchange email through different compatible providers, without one company owning the entire network?**

That became PactRide: a ride-coordination protocol proposal using user-controlled identity, replaceable relays, private negotiation, bilateral agreement, and portable evidence.

CommonPact extends the underlying idea. Ride coordination is one instance of a broader social pattern. Deliveries, rentals, donations, temporary work, local services, and other interactions also place a platform between a person seeking something and a person or organization providing it. The platform may be useful, but it becomes the mandatory owner of discovery, trust, records, and access.

## Canonical vision

CommonPact is intended to become an open coordination layer for direct agreements between people and organizations.

The protocol should allow independently developed applications to:

- discover compatible counterparties;
- negotiate terms privately;
- authorize the same agreement;
- record a profile-defined lifecycle;
- preserve claims and conflicting evidence;
- produce portable completion receipts;
- choose optional service providers;
- switch applications without losing protocol access.

CommonPact is the reusable base. Domain-specific protocols exist as profiles:

- PactRide for rides;
- PactRental for temporary asset use;
- PactDelivery for package custody and delivery;
- PactFund for donation and campaign coordination;
- future Pact profiles created through public review.

The founder does not want CommonPact to become a new mandatory super-platform. A single official application controlling all profiles would repeat the problem the project is intended to address.

## Social objective

The objective is to reduce unnecessary rent extraction and platform dependency.

CommonPact should make it possible for coordination software to compete on interface, support, safety services, hosting, payment integration, insurance, verification, moderation, and local operations without owning the underlying relationship between users.

The desired outcome is not a world with no infrastructure or no businesses. It is a world where infrastructure providers are:

- visible;
- optional at the protocol level;
- replaceable;
- interoperable;
- unable to permanently trap identity, reputation, or history;
- unable to impose a hidden protocol toll.

## Email analogy

Email is the most useful conceptual analogy, but not a literal architecture requirement.

People using Gmail, Outlook, Proton Mail, self-hosted servers, or other compatible providers can communicate because shared standards exist below the applications. Providers still run servers, filter spam, charge for services, and enforce local policies. No single provider owns email itself.

CommonPact seeks a similar separation:

- the protocol defines how a pact is expressed and verified;
- profiles define domain-specific meaning and safeguards;
- applications provide user experiences;
- transports deliver messages;
- optional providers supply specialized services;
- no single application or provider owns the protocol network.

## Peer-to-peer and mesh intent

The founder's original intuition included person-to-person and mesh-like coordination, influenced by systems such as BitChat.

CommonPact preserves that intent through transport independence and degraded-connectivity support, but it does not claim that phone-to-phone Bluetooth mesh can reliably replace internet discovery for citywide or global use.

The practical baseline is:

- internet-first discovery through multiple replaceable relays or servers;
- encrypted direct communication where available;
- local client-side matching and validation;
- nearby or peer-to-peer exchange for handoff verification, resilience, and limited offline operation;
- future research into stronger decentralized transports without making unrealistic reliability claims.

The essential goal is not "no servers." It is **no mandatory central owner**.

## Economic intent

The base protocol must not require:

- a percentage commission;
- a listing fee;
- a mandatory subscription;
- a CommonPact token;
- one wallet;
- one payment processor;
- one escrow provider;
- one identity provider;
- one relay operator;
- one official application.

Compatible applications and providers may charge transparent fees for real services. CommonPact does not define all fees as illegitimate. It distinguishes payment for optional value from unavoidable rent charged by the owner of a closed network.

## Decisions represented in this repository

The founder vision is considered documented because the repository records:

1. the platform-ownership problem;
2. the protocol-versus-platform distinction;
3. the generic pact lifecycle;
4. user-controlled identity and authorization;
5. privacy-limited discovery;
6. private proposals, counters, and agreement;
7. portable evidence, receipts, disputes, and revocations;
8. transport independence and realistic mesh limits;
9. a strict profile system;
10. the relationship to PactRide;
11. PactRental as a second-domain abstraction test;
12. PactDelivery and PactFund as candidate profiles;
13. optional-provider and no-protocol-tax economics;
14. privacy, security, legal, accessibility, and operational boundaries;
15. governance, contribution, succession, licensing, and maintenance;
16. human journeys, adoption and network-bootstrap strategy;
17. accessibility, abuse, key recovery, data portability, and legal-review boundaries;
18. machine-readable strict event schemas, cryptographic fixtures, examples, validators, and a public website;
19. a complete founder-authored PactRental profile package that tests the abstraction;
20. clear separation between documented vision and implementation evidence.

## Meaning of "100% documented"

For CommonPact, **100% founder-vision documented** means:

- every major part of the founder's current intent has a canonical repository location;
- the project can be understood without private chat history;
- the repository explains what CommonPact is, why it exists, how profiles relate to the core, and where responsibility lies;
- aspirations are separated from implemented facts;
- unresolved work is recorded as evidence gates rather than omitted;
- machine-readable artifacts and deterministic error codes are sufficient for implementers to find ambiguity;
- the core is mapped against PactRide and PactRental so ride-specific assumptions are visible;
- the GitHub Pages site accurately summarizes the repository;
- a future maintainer can continue the work without requiring the founder to restate the concept.

It does not mean:

- the protocol is correct;
- the abstraction is independently proven;
- applications or production infrastructure exist;
- any profile is legally approved or operational;
- optional providers are unnecessary;
- fraud, safety, trust, adoption, density, regulation, payment, or dispute problems are solved;
- contributors, funding, users, or partners will appear.

## Completion statement

As of 2026-07-11, this repository contains the complete initial founder vision for CommonPact as a public, pre-implementation coordination-protocol RFC.

The next work is evidence: independent review, cross-language implementations, profile validation, security analysis, transport measurements, and domain-specific expertise. Those are public roadmap gates, not missing private vision.
