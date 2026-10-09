# TRANS-UB Quality Scenarios

## QR-01 — Search performance

**Source / stimulus:** A student searches for a textbook or other approved low-risk item.  
**Environment:** TRANS-UB is operating normally.  
**Artifact:** Listing search and catalogue data.  
**Response:** Relevant approved listings are retrieved and displayed.  
**Measure:** Results are visible within 2 seconds for at least 95% of searches.

## QR-02 — Listing performance

**Source / stimulus:** A student opens a listing.  
**Environment:** TRANS-UB is operating normally.  
**Artifact:** Listing record.  
**Response:** Current product information, price, seller information and availability are displayed.  
**Measure:** Listing details are displayed within 2 seconds for at least 95% of requests.

## QR-03 — Student verification / access control

**Source / stimulus:** An unverified account attempts a protected listing action.  
**Environment:** The account exists but has not passed simulated student verification.  
**Artifact:** StudentAccount and protected listing function.  
**Response:** The action is rejected.  
**Measure:** 100% of protected listing attempts by unverified accounts are rejected.

## QR-04 — Listing validation

**Source / stimulus:** A seller submits a listing with required information missing or a prohibited category.  
**Environment:** The seller is creating or editing a listing.  
**Artifact:** Listing and approval rules.  
**Response:** The listing is rejected from publication and the reason is shown.  
**Measure:** 100% of incomplete or prohibited listings are prevented from becoming Available.

## QR-05 — Order reliability

**Source / stimulus:** An eligible buyer confirms reservation of an Available listing.  
**Environment:** TRANS-UB is operating normally.  
**Artifact:** Order and Listing.  
**Response:** Exactly one Pending order is recorded and the listing becomes Reserved as one consistent result.  
**Measure:** At least 99% of valid confirmations finish within 3 seconds without partial or lost transaction state.

## QR-06 — Duplicate reservation prevention

**Source / stimulus:** The same reservation is submitted repeatedly, or two buyers confirm the same listing concurrently.  
**Environment:** Reservation processing is active.  
**Artifact:** Order and Listing.  
**Response:** The system keeps at most one live reservation for the listing.  
**Measure:** Zero duplicate live reservations are created.

## QR-07 — Seller notification failure tolerance

**Source / stimulus:** A Pending order is created while immediate seller notification delivery fails.  
**Environment:** The notification channel is temporarily unavailable.  
**Artifact:** Notification and Order.  
**Response:** The reservation remains valid; the notification outcome is recorded for retry or later visibility.  
**Measure:** 100% of valid reservations remain stored even when immediate notification fails, and every failed notification is recorded.

## QR-08 — Listing update integrity

**Source / stimulus:** A seller edits an existing listing.  
**Environment:** The listing exists.  
**Artifact:** Listing.  
**Response:** Only the intended seller-owned listing is changed.  
**Measure:** 100% of valid listing updates affect only the intended listing.

## QR-09 — Review integrity

**Source / stimulus:** A buyer attempts to review a transaction.  
**Environment:** The linked order is not yet Completed.  
**Artifact:** Review and Order.  
**Response:** The review is rejected.  
**Measure:** 100% of reviews for non-Completed orders are rejected.

## QR-10 — Stale listing conflict

**Source / stimulus:** A buyer confirms a reservation using a view that has become stale.  
**Environment:** The listing changed after the buyer first viewed it.  
**Artifact:** Listing and Order.  
**Response:** The system rechecks current availability before creating the order and refuses the reservation if the listing is no longer Available.  
**Measure:** 100% of reservations against unavailable listing state are rejected before order creation.
