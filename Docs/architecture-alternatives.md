# TRANS-UB Architecture Alternatives Comparison

## Architecture drivers
- Prevent duplicate/conflicting reservations.
- Keep Listing and Order states consistent.
- Keep notification failure from rolling back a valid reservation.
- Enforce buyer, seller and Platform Administrator permissions.
- Keep payment and physical handover outside TRANS-UB.
- Remain simple enough for the team to implement and test.

## Alternative A-Simple Layered Monolith
One deployable application with presentation, service/business and persistence layers.

Strengths:
- Lowest implementation complexity.
- Easy to deploy and test.
- Strong single-process transaction support.

Weaknesses:
- Higher coupling.
- Business rules can become scattered.
- Data ownership and failure boundaries are less clear.

## Alternative B-Modular Layered Monolith
One deployable application divided into explicit modules:
Account, Listing, Order/Reservation, Review, Reporting/Moderation, Notification and Persistence.

Strengths:
- Clearer responsibilities and interfaces.
- Lower coupling.
- Better requirement-to-module traceability.
- Strong transaction support without distributed-system complexity.
- Easier testing and future evolution.

Weaknesses:
- More initial design work.
- Requires discipline to preserve module boundaries.

## Comparison

| Criterion | Simple Layered Monolith | Modular Layered Monolith |
|---|---|---|
| Implementation effort | Lower | Moderate |
| Transaction consistency | Strong | Strong |
| Coupling | Higher | Lower |
| Responsibility clarity | Moderate | Strong |
| Security-boundary clarity | Moderate | Strong |
| Failure isolation | Limited | Better |
| Maintainability | Moderate | Strong |
| Prototype suitability | Strong | Strong |
| Future evolution | Limited | Better |

## Preferred direction
Use a modular layered monolith. It keeps deployment simple while giving TRANS-UB clearer ownership of listing, reservation, review, reporting and notification responsibilities.
