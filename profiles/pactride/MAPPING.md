# PactRide to CommonPact Mapping

**Status:** explanatory, non-normative, no runtime dependency

| PactRide | Candidate CommonPact concept |
|---|---|
| rider and driver | profile-defined parties and roles |
| `ride_id` | `pact_id` aggregate identifier |
| independent driver offer | negotiation thread |
| coarse ride request | expiring public intent |
| encrypted exact locations and terms | private negotiation |
| `ride.offer` / `ride.counter` | complete proposal / counter |
| matching acceptance over terms | canonical agreement |
| pickup proof | profile activation proof |
| departure, arrival, in-progress | profile lifecycle updates |
| ride cancellation | pre-activation cancellation |
| ride abort | post-activation abnormal termination |
| completion claim | unilateral completion claim |
| bilateral completion receipt | profile completion receipt |
| ride dispute | preserved conflict state |
| vehicle and identity claims | external attestations |
| local reputation policy | client-side trust evaluation |

## Ride-specific safeguards that do not become generic

- pickup and destination privacy;
- geospatial discovery policy;
- rider and driver licensing and insurance;
- vehicle category and accessibility requirements;
- driver departure and arrival;
- pickup challenge procedure;
- road safety and emergency response;
- live route and trip progress;
- transportation cancellation timing;
- ride-market density and dispatch behavior.

## Compatibility rule

A CommonPact implementation is not automatically PactRide-compatible. A PactRide implementation does not need CommonPact. Existing events must never be silently renamed or reinterpreted.
