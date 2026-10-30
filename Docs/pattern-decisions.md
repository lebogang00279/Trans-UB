# TRANS-UB Lab 9 — Pattern Decisions

## Traceability
Core workflow: **UC-05 — Reserve an Available Listing**  
Related requirements: FR-05, FR-07, FR-08 and duplicate-reservation / notification-failure quality concerns.

| Project problem | Decision | Participants | Why it fits | Cost |
|---|---|---|---|---|
| Persistence coupling | Repository interfaces | `ListingRepository`, `OrderRepository`, `OrderStatusChangeRepository`, persistence adapter | Core workflow depends on stable interfaces instead of DB-specific code. | More interfaces/adapters. |
| Reservation workflow coordination | Application Service / Service Layer | `ReservationService`, domain entities, repository ports | Gives UC-05 one clear coordinator and transaction boundary. | Service must stay focused. |
| Notification failure | Dependency Inversion with `NotificationPort` | `ReservationService`, `NotificationPort`, notification adapter | Notification failure does not corrupt a successful reservation. | Requires adapter and retry/error handling. |

## Repository interfaces
`ReservationService` depends on repository ports, not SQL/JDBC/ORM details.

## Reservation application service
A successful reservation coordinates:
1. buyer validation;
2. final availability check;
3. creation of Pending Order;
4. initial OrderStatusChange;
5. Listing Available -> Reserved;
6. commit of core state;
7. seller notification.

## Notification port
Core code depends on:
```text
NotificationPort
  notifySellerReservation(...)
```
The concrete delivery mechanism remains outside the core workflow.

## Explicit rejection — Full State Pattern
A full State pattern is rejected for now. The Order lifecycle is still small enough to manage with controlled domain methods:
`accept()`, `reject()`, `cancel()`, `expire()`, `markDelivered()`, `confirmReceipt()`.

Separate state classes would add accidental complexity without enough state-specific behavior to justify them.

## Verification
- only one live reservation succeeds per Listing;
- notification failure does not reverse a successful reservation;
- invalid Order transitions are rejected;
- repository failure does not leave partial reservation state.
