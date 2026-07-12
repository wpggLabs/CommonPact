# Core and Profile Mapping

This matrix tests whether CommonPact is a real abstraction rather than PactRide terminology with renamed fields.

| CommonPact concept | PactRide realization | PactRental realization | Must remain profile-specific |
|---|---|---|---|
| Participant roles | rider, driver | owner, renter, optional custodian | authority, licensing, domain duties |
| Public intent | coarse ride request or availability | asset category and broad availability | location precision, asset detail, risk filters |
| Negotiation thread | one driver offer thread | one renter/owner negotiation | domain terms and disclosure timing |
| Complete terms | pickup, destination, fare, accommodations | asset, period, price, deposit, permitted use | domain-specific obligations |
| Acceptance | rider and driver authorize terms hash | owner and renter authorize terms hash | required roles and timing |
| Activation proof | pickup verification | asset handoff and condition evidence | physical procedure and evidence fields |
| Progress | departure, arrival, in-progress | in-use, extensions, maintenance events | allowed authors and state meanings |
| Pre-activation end | ride cancellation | reservation cancellation | refund and notice rules |
| Post-activation end | ride abort | early termination or asset recovery | safety, possession, liability |
| Completion claim | one party claims trip complete | one party claims asset returned | claim contents |
| Completion receipt | bilateral trip receipt | bilateral return receipt | signer set and outcome fields |
| Dispute | conflicting ride evidence | condition, damage, or possession dispute | remedies and domain experts |
| External evidence | vehicle/identity attestations | ownership, inspection, insurance attestations | credential authority and legal effect |
| Portable history | ride receipts and attestations | rental receipts and condition evidence | selective disclosure and retention |
| Optional services | maps, payments, insurance, support | escrow, inspections, insurance, support | deployment requirements |

## Extraction conclusion

The shared pattern is signed coordination: discover, negotiate, authorize, activate, progress, claim, receive, dispute, and export. Physical meaning remains in profiles.

No PactRide event is silently reinterpreted as CommonPact wire format. PactRide remains standalone until a future explicit RFC chooses an adapter or major-version migration.
