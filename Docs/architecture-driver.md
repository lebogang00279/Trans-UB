# TRANS-UB Architecture Drivers

The Phase 2 architecture drivers come from the Phase 1 quality scenarios and constraints, not from a preferred framework.

## Driver 1 — Transaction consistency and duplicate-reservation prevention

**Sources:** FR-05, UC-05, QR-05, QR-06 and QR-10.

A successful reservation must create exactly one Pending Order and move the Listing from Available to Reserved without allowing a second live reservation.

**Architecture obligation:** Order creation and Listing reservation need one consistency boundary.

## Driver 2 — Access control and trust integrity

**Sources:** FR-01, FR-03, FR-09, QR-03 and QR-09.

Protected actions require eligible accounts, listings require moderation, and reviews require a Completed transaction.

**Architecture obligation:** authorization and lifecycle guards must be enforced beyond the user interface and remain reusable across workflows.

## Driver 3 — Reliability under partial failure

**Sources:** UC-05 notification alternative and QR-07.

A notification failure must not undo a valid reservation, while stale listing state must be detected before creating an order.

**Architecture obligation:** core transaction state and notification delivery must be separated so notification can be retried safely.

## Alternative A — Simple layered monolith

One deployable application with presentation, application/service, domain and persistence layers.

**Advantages**
- Lowest deployment complexity.
- Straightforward local transactions across Order and Listing.
- Suitable for a semester-scale prototype.

**Disadvantages**
- Responsibility boundaries may become weak if all features accumulate in shared services.
- Moderation, order and notification concerns can become tightly coupled.

## Alternative B — Modular layered monolith

One deployable application, but marketplace, ordering, moderation and notification are separated into modules with explicit interfaces.

**Advantages**
- Preserves the Phase 1 responsibility boundaries.
- Keeps simple local transaction handling for reservation consistency.
- Easier to test and evolve by module than an undifferentiated monolith.

**Disadvantages**
- More internal interfaces and design discipline are required.
- Slightly more design effort.