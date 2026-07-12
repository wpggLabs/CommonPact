# Accessibility

Accessibility is a profile and application requirement, not an optional website feature.

## Core expectations

CommonPact events SHOULD support machine-readable accessibility requirements without requiring public diagnosis disclosure. Profiles MUST separate functional needs from sensitive medical detail and define when information becomes visible.

## Profile requirements

Each profile MUST document:

- functional accommodations relevant to the domain;
- public, private-before-agreement, and private-after-agreement fields;
- how accommodations become part of canonical terms;
- who may accept or decline a requirement;
- how failure to provide an agreed accommodation is recorded;
- nonvisual and low-bandwidth alternatives to QR, maps, images, or audio;
- additional time, communication, mobility, language, or support needs;
- accessibility-specific privacy and discrimination risks.

## Client expectations

Compatible clients SHOULD meet WCAG 2.2 AA for web surfaces or corresponding platform guidance, support keyboard and assistive technology operation, preserve text scaling, avoid color-only meaning, provide reduced-motion behavior, and expose signed terms in understandable language before authorization.

## Protocol boundary

A signature does not prove an accommodation was provided. Profiles may preserve commitments and evidence, while accountable operators remain responsible for accessible service and applicable law.
