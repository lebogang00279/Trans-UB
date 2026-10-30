# TRANS-UB Lab 9 — Framework and Dependency-Management Decision

## Decision
Keep the core application/domain design **framework-neutral**.

Use:
- plain Java interfaces for ports;
- constructor-based dependency injection;
- adapters for persistence and notification technology;
- `ReservationService` as the UC-05 application-service boundary.

## Dependency direction
```text
UI / Controller
      |
      v
ReservationService
      |
      +--> ListingRepository <--- Persistence Adapter
      +--> OrderRepository   <--- Persistence Adapter
      +--> NotificationPort  <--- Notification Adapter
      |
      v
Domain entities
```

## Rationale
This preserves the modular layered monolith, supports testing, and prevents persistence or notification technology from leaking into the domain.

## Explicit rejection
Do not introduce microservices, an event broker, or a dependency-injection framework only to satisfy Lab 9. They add deployment/configuration complexity without solving a current TRANS-UB requirement better than the existing modular monolith.

## Revisit trigger
Revisit when the implementation stack is formally selected or manual dependency wiring becomes a significant maintenance cost.
