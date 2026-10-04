TRANS-UB Core API / Service Contract

Operation

Reserve an Available Listing

Traceability

This operation supports the TRANS-UB Phase 1 baseline:

• FR-05 — Buyer reserves/orders an Available listing.
• UC-05 — Reserve an Available Listing.
• Quality concerns:
  • duplicate reservation prevention;
  • order reliability;
  • stale listing conflict handling;
  • transaction consistency.

Endpoint

POST /api/listings/{listingId}/reserve

Purpose

Allows an eligible Student Buyer to reserve an approved listing that is currently Available.

A successful reservation:

1. creates a new Order with status Pending;
2. records an OrderStatusChange from no previous state to Pending;
3. changes the Listing from Available to Reserved;
4. sets the seller response deadline to 24 hours after reservation;
5. raises a seller notification.

Payment and physical handover remain outside TRANS-UB.

Request

Path parameter

|Name       |Type  |Required|Description                                       |
|-----------|------|-------:|--------------------------------------------------|
|`listingId`|String|Yes     |Identifies the listing the buyer wants to reserve.|

Request body

{
  "buyerId": "202302072",
  "buyerNote": "I would like to collect this on campus."
}

Request fields

|Field      |Type  |Required|Description                                         |
|-----------|------|-------:|----------------------------------------------------|
|`buyerId`  |String|Yes     |Identifies the Student Buyer making the reservation.|
|`buyerNote`|String|No      |Optional note from the buyer to the seller.         |

Validation

Before creating the reservation, the service must verify that:

1. the buyer account exists;
2. the buyer account is active and eligible;
3. the listing exists;
4. the listing is approved;
5. the listing status is Available;
6. the buyer is not the seller of the listing;
7. there is no existing live reservation for the listing.

The service must perform a final availability check immediately before creating the Order. This protects against two buyers attempting to reserve the same listing at nearly the same time.

Business Rules

Successful reservation

When all validation rules pass:

Order.status = Pending
Order.responseDeadline = current time + 24 hours
Listing.status: Available -> Reserved
OrderStatusChange: none -> Pending

The reservation-related state changes must be treated as one atomic operation.

The core transaction includes:

1. re-check listing availability;
2. create the Pending Order;
3. create the OrderStatusChange;
4. change the Listing from Available to Reserved;
5. commit the transaction.

If any required state change fails, the reservation must not be partially committed.

Notification handling

After the reservation succeeds, the system raises a notification for the seller.

A notification delivery failure must not roll back the reservation.

The system should record the notification delivery outcome so that a failed notification can be retried.

Successful Response

HTTP status

201 Created

Example response

{
  "orderReference": "ORD-2026-00125",
  "listingId": "LIST-104",
  "buyerId": "202302072",
  "status": "Pending",
  "listingStatus": "Reserved",
  "responseDeadline": "2026-10-05T23:00:00+02:00",
  "message": "Reservation created successfully."
}

Error Outcomes

|HTTP Status                |Error Code             |Meaning                                           |
|---------------------------|-----------------------|--------------------------------------------------|
|`400 Bad Request`          |`INVALID_REQUEST`      |Required request data is missing or invalid.      |
|`401 Unauthorized`         |`UNAUTHENTICATED`      |The user is not authenticated.                    |
|`403 Forbidden`            |`BUYER_NOT_ELIGIBLE`   |The buyer account is inactive or not eligible.    |
|`403 Forbidden`            |`OWN_LISTING`          |The buyer attempted to reserve their own listing. |
|`404 Not Found`            |`LISTING_NOT_FOUND`    |The requested listing does not exist.             |
|`409 Conflict`             |`LISTING_NOT_AVAILABLE`|The listing is no longer Available.               |
|`409 Conflict`             |`DUPLICATE_RESERVATION`|A live reservation already exists for the listing.|
|`500 Internal Server Error`|`RESERVATION_FAILED`   |The reservation could not be completed safely.    |

Example conflict response

{
  "error": "LISTING_NOT_AVAILABLE",
  "message": "This listing is no longer available.",
  "currentStatus": "Reserved"
}

Failure and Recovery Behaviour

Simultaneous reservation requests

If two buyers attempt to reserve the same Available listing at nearly the same time, only one request may succeed.

Expected outcome:

Buyer A:
Reservation succeeds
Order A -> Pending
Listing -> Reserved

Buyer B:
Final availability check fails
No Order B is created
Response -> 409 LISTING_NOT_AVAILABLE

This prevents duplicate Pending orders and inconsistent Listing state.

Notification failure

If seller notification delivery fails after a successful reservation:

Order remains Pending
Listing remains Reserved
Notification failure is recorded
Notification may be retried

The reservation is not reversed.

Data Integrity Constraints

The operation must preserve the following constraints:

• one listing must not have more than one live reservation at the same time;
• a Pending Order created by this operation must correspond to a Reserved Listing;
• a failed reservation must not leave a partial Order or state change;
• notification failure must not corrupt Order or Listing state;
• the buyer must not reserve their own listing.

Architectural Responsibilities

|Responsibility                                  |Owning module                              |
|------------------------------------------------|-------------------------------------------|
|Validate buyer identity and account eligibility |Account / Authentication                   |
|Check listing status and ownership              |Listing Management                         |
|Create Order and control order-state transitions|Order / Reservation                        |
|Coordinate Listing and Order consistency        |Order / Reservation with Listing Management|
|Record status history                           |Order / Reservation / Persistence          |
|Send seller notification                        |Notification                               |
|Persist reservation-related data                |Persistence / Database Access              |

Normal Outcome Summary

Available Listing

      |
      | POST /api/listings/{listingId}/reserve
      v

Final availability check

      |
      v

Create Pending Order

      |
      v

Record OrderStatusChange

      |
      v

Listing -> Reserved

      |
      v

Commit transaction

      |
      v

Raise seller notification

      |
      v

201 Created

Main Integrity Risk

The main integrity risk is two buyers reserving the same listing concurrently.

The service contract addresses this by requiring a final availability check and atomic persistence of the Order, OrderStatusChange, and Listing status update.
