# Key Management and Recovery

Keys authorize protocol events. Poor recovery design can either permanently lock users out or recreate a mandatory identity provider.

## Device keys

Clients SHOULD use hardware-backed storage where available, encrypt local state, minimize key export, and support multiple authorized devices through scoped delegation rather than uncontrolled key copying.

## Recovery options

A deployment MAY support recovery codes, social recovery, delegated guardians, organization administrators, threshold keys, hardware tokens, or a commercial recovery provider. No recovery provider is mandatory at the core layer.

## Rotation and compromise

Rotation MUST reference old and new identities, effective time, scope, and proof requirements. Compromise events SHOULD identify affected keys and time ranges. Historical signatures remain verifiable but local policy may lower confidence after compromise.

## Delegation

Delegations MUST be least-privilege, profile-scoped, event-scoped where possible, expiring, revocable, and visible before authorization. Employee, fleet, courier, guardian, and automated-agent delegation require profile-specific authority rules.

## Loss and continuity

A lost key may mean loss of future control. Portable receipts can remain verifiable without giving a recovery provider power to rewrite history. Clients MUST explain this distinction clearly.
