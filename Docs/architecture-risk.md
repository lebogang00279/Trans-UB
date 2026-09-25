# TRANS-UB Highest Architectural Risk

## Risk
Inconsistent Listing and Order state during simultaneous reservation attempts.

## Why it matters
Two buyers may attempt to reserve the same Available listing at nearly the same time. Without an atomic update, more than one live Pending order could be created.

## Architectural response
The Order / Reservation module must:
1. Re-check that the Listing is still Available.
2. Create the Pending Order.
3. Record the OrderStatusChange.
4. Change Listing from Available to Reserved.
5. Commit all required changes atomically.
6. Reject a competing request if the Listing is no longer Available.

## Failure boundary
Notification delivery is outside the core reservation transaction. A notification failure must be recorded and retried, but must not undo a valid reservation.

## Verification
Run an integration test with two near-simultaneous reservation requests for the same listing. Expected result:
- exactly one Pending Order;
- Listing is Reserved;
- the competing request is rejected.
