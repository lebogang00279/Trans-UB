TRANS-UB Lab 5 Consistency Matrix

Core workflow

Selected use case: UC-05 — Reserve an available listing

This matrix links the UC-05 use-case steps to the interaction messages, responsible analysis/domain elements, lifecycle states and requirements. The same names and IDs should be used in the sequence diagram, state-machine/activity model and Phase 1 report.

|Matrix ID|Requirement          |Use-case step / condition                                                                                                  |Sequence message to use                          |Responsibility / analysis element                          |State / transition                                             |Verification                                                                                                                            |
|---------|---------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|-----------------------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|CM-01    |FR-01                |Precondition: buyer is signed in and simulated Student-ID verification passed.                                             |`validateBuyer()`                                |Student Buyer; Account; TRANS-UB Hub                       |Buyer account must be Active                                   |Try UC-05 with a valid active prototype account and with an invalid/suspended account. Only the eligible buyer may continue.            |
|CM-02    |FR-03                |Precondition: listing has been approved by the administrator.                                                              |`checkListingApproval()`                         |Listing; Platform Administrator; TRANS-UB Hub              |Listing must not be `Pending Approval` or removed              |Attempt to reserve an unapproved/removed listing. No order must be created.                                                             |
|CM-03    |FR-04, FR-05         |UC-05 Step 1: buyer opens an approved listing and asks to reserve it.                                                      |`requestReservation(listingId)`                  |Student Buyer; Listing; TRANS-UB Hub                       |Listing expected state: `Available`                            |Open an approved available listing and request reservation.                                                                             |
|CM-04    |FR-05                |UC-05 Step 2: hub checks that the listing is still available.                                                              |`checkAvailability(listingId)`                   |Listing; TRANS-UB Hub                                      |Guard: `[listing.status == Available]`                         |Attempt reservation after another buyer has already reserved the item. Request must fail and no second order may be created.            |
|CM-05    |FR-01, FR-05         |UC-05 Step 2: hub confirms that the buyer is eligible and is not the seller.                                               |`checkReservationEligibility(buyerId, listingId)`|Student Buyer; Student Seller; Listing; TRANS-UB Hub       |Guard: buyer Active and `buyer != seller`                      |Seller attempts to reserve own listing; system must reject the request.                                                                 |
|CM-06    |FR-05, Decision D-001|UC-05 Step 3: hub explains reservation rules, 24-hour seller response, cancellation, offline payment and physical handover.|`showReservationTerms()`                         |TRANS-UB Hub; Student Buyer                                |No state change                                                |Verify the confirmation screen states that payment and handover occur outside TRANS-UB and recommends a public campus handover location.|
|CM-07    |FR-05                |UC-05 Step 4: buyer confirms the reservation and may add a note.                                                           |`confirmReservation(note)`                       |Student Buyer; TRANS-UB Hub                                |Request accepted for processing                                |Confirm with and without an optional handover note.                                                                                     |
|CM-08    |FR-05                |UC-05 Step 5: hub creates one order linked to buyer, seller and listing.                                                   |`createOrder(buyerId, sellerId, listingId, note)`|Order; Student Buyer; Student Seller; Listing; TRANS-UB Hub|Order: `New → Pending`                                         |Verify exactly one Pending order is created and linked to exactly one buyer, one seller and one listing.                                |
|CM-09    |FR-05                |UC-05 Step 5: hub reserves the listing.                                                                                    |`markListingReserved()`                          |Listing; Order; TRANS-UB Hub                               |Listing: `Available → Reserved`                                |Verify the listing changes to Reserved and is no longer reservable by another buyer.                                                    |
|CM-10    |FR-07                |UC-05 Step 5: hub records the seller response deadline.                                                                    |`setResponseDeadline(24h)`                       |Order; TRANS-UB Hub                                        |Order remains `Pending`; deadline recorded                     |Verify the deadline is exactly 24 hours from order creation.                                                                            |
|CM-11    |FR-05                |UC-05 Step 5: status change is recorded for auditability.                                                                  |`recordStatusChange(Pending)`                    |Order History; Order; TRANS-UB Hub                         |History entry: `Pending` with actor/time                       |Verify order history contains the new status, actor and timestamp.                                                                      |
|CM-12    |FR-05                |UC-05 Step 6: seller is informed that a Pending order exists.                                                              |`notifySeller(orderId)`                          |Student Seller; Order; TRANS-UB Hub                        |Order stays `Pending`                                          |Verify seller can see the Pending order. If immediate notification fails, the order must remain valid.                                  |
|CM-13    |FR-05                |UC-05 Step 6: buyer is shown the order reference, status and deadline.                                                     |`showReservationConfirmation(orderId)`           |Student Buyer; Order; TRANS-UB Hub                         |Order stays `Pending`; Listing stays `Reserved`                |Verify buyer sees the order reference, Pending status and deadline.                                                                     |
|CM-14    |FR-05                |Extension 2a/2b/2f: listing is no longer eligible or available before confirmation.                                        |`rejectReservation(reason)`                      |Listing; TRANS-UB Hub                                      |No new order; listing keeps its current state                  |Change/remove/reserve the listing before buyer confirmation. Verify no order is created and buyer receives a clear reason.              |
|CM-15    |FR-05                |Extension 2e: buyer already has a Pending order for the same listing.                                                      |`findExistingPendingOrder()`                     |Order; Student Buyer; Listing; TRANS-UB Hub                |Existing Order remains `Pending`; no duplicate state           |Double-submit the same reservation. Verify the existing order is returned and no duplicate order is created.                            |
|CM-16    |FR-05                |Extension 5a: two buyers confirm almost simultaneously.                                                                    |`reserveAtomically()`                            |Listing; Order; TRANS-UB Hub                               |Exactly one `Available → Reserved`; one Order becomes `Pending`|Simulate two simultaneous requests. Exactly one must succeed.                                                                           |
|CM-17    |FR-05                |Extension 5b: order cannot be stored.                                                                                      |`rollbackReservation()`                          |Order; Listing; TRANS-UB Hub                               |No Order created; Listing remains `Available`                  |Force order-save failure. Verify no half-written reservation and listing remains Available.                                             |
|CM-18    |FR-05                |Extension 6a: seller notification fails.                                                                                   |`retrySellerNotification()`                      |Student Seller; Order; TRANS-UB Hub                        |Order remains `Pending`; Listing remains `Reserved`            |Simulate notification failure. Verify reservation is not rolled back and seller can still see the order later.                          |

Follow-on lifecycle consistency

These rows connect the state created by UC-05 to the requirements that resolve it after the core reservation use case ends.

|Matrix ID|Requirement|Related use case / event                         |Sequence message to use                 |Responsibility / analysis element                             |State / transition                                                                        |Verification                                                                                                                        |
|---------|-----------|-------------------------------------------------|----------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
|CM-19    |FR-06      |Seller accepts Pending order.                    |`acceptOrder(orderId)`                  |Student Seller; Order; Listing; TRANS-UB Hub                  |Order: `Pending → Accepted`; Listing stays `Reserved`                                     |Accept a Pending order and verify its status changes to Accepted while the listing remains Reserved.                                |
|CM-20    |FR-06      |Seller rejects Pending order.                    |`rejectOrder(orderId)`                  |Student Seller; Order; Listing; TRANS-UB Hub                  |Order: `Pending → Rejected`; Listing: `Reserved → Available`                              |Reject a Pending order and verify the listing is released.                                                                          |
|CM-21    |FR-07      |Seller gives no response for 24 hours.           |`expireOrder(orderId)`                  |Order; Listing; TRANS-UB Hub                                  |Order: `Pending → Expired`; Listing: `Reserved → Available`                               |Advance/reach the response deadline and verify automatic expiry and release of the listing.                                         |
|CM-22    |FR-07      |Buyer cancels before physical handover.          |`cancelOrder(orderId)`                  |Student Buyer; Order; Listing; TRANS-UB Hub                   |Order: `Pending/Accepted → Cancelled`; Listing: `Reserved → Available`                    |Cancel before handover and verify the order is Cancelled and listing returns to Available.                                          |
|CM-23    |FR-08      |Seller records physical handover.                |`markDelivered(orderId)`                |Student Seller; Order; TRANS-UB Hub                           |Order: `Accepted → Delivered`; Listing stays `Reserved`                                   |Mark an accepted order Delivered and verify the state change.                                                                       |
|CM-24    |FR-08      |Buyer confirms receipt.                          |`confirmReceipt(orderId)`               |Student Buyer; Order; Listing; TRANS-UB Hub                   |Order: `Delivered → Completed`; Listing: `Reserved → Sold`                                |Confirm receipt and verify the order becomes Completed and the listing is no longer available.                                      |
|CM-25    |FR-09      |Buyer submits one review after completion.       |`submitReview(orderId, rating, comment)`|Student Buyer; Review; Order; Student Seller; TRANS-UB Hub    |Guard: `[order.status == Completed]`                                                      |Verify review is rejected before completion and exactly one review is accepted after completion.                                    |
|CM-26    |FR-10      |Buyer or seller reports a listing, user or order.|`submitReport(targetId, reason)`        |Student Buyer/Seller; Report; Listing/Order; TRANS-UB Hub     |Report: `New → Open`; order/listing state unchanged unless admin acts                     |Submit a report and verify it is stored without automatically changing the transaction state.                                       |
|CM-27    |FR-10      |Administrator reviews and resolves report.       |`resolveReport(reportId, resolution)`   |Platform Administrator; Report; Account; Listing; TRANS-UB Hub|Report: `Open → Resolved` (or escalated); related account/listing may be suspended/removed|Verify administrator can record a resolution and apply an allowed moderation action or escalate a serious unresolved dispute to SRC.|

State vocabulary to keep consistent

Order states

Pending -> Accepted -> Delivered -> Completed

Alternative terminal paths:

• Pending -> Rejected
• Pending -> Expired
• Pending -> Cancelled
• Accepted -> Cancelled before physical handover

Listing states

Pending Approval -> Available -> Reserved -> Sold

Release paths:

• Reserved -> Available after Rejected, Expired or Cancelled

Consistency notes

1. FR-05 means reserve/order an available listing. It does not require a shopping cart.
2. FR-06 means seller acceptance or rejection.
3. FR-07 means reservation expiry and buyer cancellation.
4. FR-08 means seller marks Delivered and buyer confirms receipt to reach Completed.
5. FR-09 allows one review only for a Completed order.
6. FR-10 covers reporting, administrator resolution, moderation and SRC escalation.
7. Accepted and Sold are used to close lifecycle gaps already identified in UC-05. The team should formally adopt these names in the state model and related documents, or replace them everywhere with the agreed alternatives.
8. Payment and physical handover remain outside TRANS-UB under Decision D-001.
9. Student-ID verification is simulated with synthetic test data and must not be presented as an integration with official UB records.

Required cross-artifact naming

Use the same labels in all Lab 5 artefacts:

• Use case: UC-05 — Reserve an available listing
• Requirement: FR-05 — Reserve or order an item
• Core order state: Pending
• Core listing transition: Available → Reserved
• Main interaction message: requestReservation(listingId)
• Order creation message: createOrder(...)
• Listing update message: markListingReserved()
• Deadline message: setResponseDeadline (24h)