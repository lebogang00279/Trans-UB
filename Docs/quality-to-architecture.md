TRANS-UB Quality-to-Architecture Mapping

Purpose

This document translates the selected Phase 1 quality scenarios into concrete architectural obligations for TRANS-UB. It shows how each important quality concern influences the architecture, module responsibilities, interfaces, data ownership and failure handling.

Quality Scenario to Architecture Mapping

|Quality concern / scenario            |Architectural obligation                                                                       |Architectural response                                                                                                                                                  |Main modules / interfaces affected                          |
|--------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
|Prevent duplicate reservations        |The system must ensure that only one live reservation can exist for a listing at a time.       |Re-check listing availability immediately before reservation, create the Pending Order and change Listing from Available to Reserved within one atomic transaction.     |Order / Reservation, Listing Management, Persistence        |
|Maintain Listing and Order consistency|Listing state and Order state must not contradict each other.                                  |Order / Reservation coordinates state transitions with Listing Management. Reservation succeeds only when both Order and Listing changes complete successfully.         |Order / Reservation, Listing Management                     |
|Handle stale availability             |A buyer may attempt to reserve a listing that has just been reserved by someone else.          |The system performs a final availability check at confirmation time and rejects the request if the listing is no longer Available.                                      |Presentation, Order / Reservation, Listing Management       |
|Seller response deadline              |A Pending order must not remain unresolved indefinitely.                                       |Store a response deadline and support automatic transition from Pending to Expired after 24 hours of no seller response. The listing is then released back to Available.|Order / Reservation, Persistence                            |
|Notification failure tolerance        |Failure to send a notification must not cancel a valid reservation.                            |Notification is invoked after the core reservation transaction succeeds. Delivery outcome is recorded separately and failed delivery can be retried.                    |Order / Reservation, Notification                           |
|Role-based access control             |Buyers, sellers and administrators must only perform actions permitted for their roles.        |Account / Authentication validates identity, account status and permissions before protected operations are executed.                                                   |Account / Authentication, Presentation, all business modules|
|Listing moderation                    |Only approved listings should become available to buyers.                                      |Listing Management separates listing creation from approval. Platform Administrator actions control transitions to Available or Removed.                                |Listing Management, Reporting / Moderation                  |
|Review integrity                      |Reviews must only be submitted after a completed transaction and only once per eligible order. |Review Management verifies Order = Completed and checks that no previous review exists before accepting a new review.                                                   |Review Management, Order / Reservation, Persistence         |
|Report and dispute handling           |Reports must have controlled lifecycle and administrator ownership.                            |Reporting / Moderation owns Open, Under Review, Resolved and Escalated report states and exposes escalation to SRC when required.                                       |Reporting / Moderation, Account, Listing, Order             |
|Security of prototype identity        |Student verification must be simulated and must not imply integration with official UB systems.|Authentication uses prototype/synthetic identity data behind a clearly defined interface. No dependency on official UB student records is introduced.                   |Account / Authentication                                    |
|Maintainability                       |Changes in one feature area should have limited impact on unrelated areas.                     |Use a modular layered monolith with explicit modules and controlled interfaces instead of one shared service layer.                                                     |All modules                                                 |
|Traceability                          |Architecture should be easy to relate back to requirements and quality scenarios.              |Each module owns a defined set of responsibilities corresponding to Phase 1 requirements and quality concerns.                                                          |All modules                                                 |
|Simple deployment                     |The student prototype should remain easy to build, run and demonstrate.                        |Keep the system as one deployable application rather than distributed microservices.                                                                                    |Whole system                                                |
|Offline payment and handover boundary |Payment and physical exchange must remain outside the platform.                                |No Payment or Handover service is included in the application architecture. The platform records transaction state only.                                                |System boundary, Order / Reservation                        |

Resulting Architecture Obligations

The quality scenarios lead to the following architecture obligations:

1. Order / Reservation Management must control reservation consistency.
It is responsible for Pending, Accepted, Rejected, Expired, Cancelled, Delivered and Completed order transitions.
2. Listing Management must own listing state.
It controls Pending Approval, Available, Reserved, Sold and Removed states.
3. Reservation creation must be atomic.
Creating a Pending Order and changing a Listing from Available to Reserved must succeed or fail together.
4. Notification must be outside the core reservation transaction.
Notification failure must not undo a successfully created reservation.
5. Authentication and authorization must be checked before protected actions.
Buyer, seller and administrator responsibilities must remain separated.
6. Review Management must depend on completed-order evidence.
A review is permitted only after the related Order reaches Completed.
7. Reporting / Moderation must own report lifecycle and escalation.
SRC is an external participant for escalated serious disputes, not a general system administrator.
8. Persistence must support concurrency control.
The data layer must prevent more than one live reservation for the same listing during competing requests.
9. Payment and physical handover remain outside the architecture.
This follows D-001 and avoids adding unsupported payment or handover services.

Highest Architecture-Sensitive Quality Concern

The most important quality concern is transaction consistency during simultaneous reservation attempts.

If two buyers try to reserve the same Available listing at almost the same time, the architecture must guarantee that only one request succeeds. The second request must detect that the listing is no longer Available and return a refusal without creating another live Pending Order.

This concern directly influences:

• module boundaries

• transaction handling

• persistence design

• concurrency control

• integration testing

• failure handling

Relationship to ADR-001

These quality-to-architecture obligations support the decision recorded in decisions/ADR-001-architecture.md to use a modular layered monolith. This structure keeps the prototype simple to deploy while providing clearer module ownership, lower coupling and stronger control over critical state transitions.
