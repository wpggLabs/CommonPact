# Data Portability

Portability is a core social goal: users should be able to change compatible applications without losing protocol access or their verifiable records.

## Export package

A client SHOULD export:

- accepted pacts and complete canonical terms;
- lifecycle events and causal references;
- claims, receipts, disputes, attestations, warnings, and revocations;
- profile manifests and versions needed for interpretation;
- proof and verification-method metadata;
- local labels and notes separately from signed protocol evidence;
- an integrity manifest covering exported files.

## Import behavior

An importing client MUST verify evidence independently, preserve provenance, report unsupported profiles or extensions, avoid converting local notes into signed facts, and retain conflicting valid evidence.

## Selective disclosure

Users SHOULD be able to disclose a receipt or attestation without publishing their entire history. Profiles must document fields that can be redacted, derived, or proven selectively and the resulting linkability risks.

## Deletion and retention

Deleting local data does not erase copies held by counterparties, relays, providers, or authorities. Clients MUST explain retention and replication honestly. Deployments should minimize public data and publish retention policies.

## Portability test

A profile is not meaningfully portable until one client can export a pact package and an independently written client can import and validate it without contacting a canonical CommonPact service.
