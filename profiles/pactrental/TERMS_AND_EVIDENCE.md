# PactRental Terms and Evidence

## Canonical terms object

The machine-readable schema is in `schemas/pactrental-profile.schema.json`. Agreement-affecting fields are hashed as one complete object.

## Condition evidence

Condition evidence may include hashes of images, video, inspection documents, meter readings, odometer values, accessory inventories, and signed declarations. Public events should contain hashes or coarse summaries rather than sensitive raw media.

## Handoff evidence

Handoff binds the accepted terms and baseline evidence. Nearby QR, short code, NFC, Bluetooth, or direct exchange may assist verification, but no physical channel is mandatory in the base profile.

## Return evidence

Return evidence records time, possession transfer, condition declaration, usage summary, and exceptions. Delayed discovery of damage may be referenced later; it does not retroactively rewrite the signed return receipt.

## Settlement declaration

Allowed states are descriptive, such as `not_applicable`, `pending_external`, `reported_paid`, `reported_refunded`, `reported_released`, or `disputed_external`. The protocol does not assert payment finality.
