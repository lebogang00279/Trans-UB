# TRANS-UB Acceptance Criteria

These criteria use the authoritative FR-01 to FR-10 baseline and the direct UC-05 reservation workflow. The Phase 1 baseline does **not** use a shopping cart.

## AC-01 — Registration and login (FR-01)

**Given** a student uses valid synthetic student verification data  
**When** the student completes prototype registration  
**Then** the system creates an eligible account.

**Given** an account is registered and active  
**When** correct credentials are supplied  
**Then** the user is logged in.

**Given** invalid synthetic verification data  
**When** registration is attempted  
**Then** registration is rejected.

## AC-02 — Listing creation and editing (FR-02)

**Given** an eligible seller  
**When** the seller submits a complete low-risk physical-good listing  
**Then** the listing is stored for approval.

**Given** a prohibited or incomplete listing  
**When** the seller submits it  
**Then** publication is rejected or the listing remains unavailable to buyers.

## AC-03 — Listing moderation (FR-03)

**Given** a listing awaiting approval  
**When** the Platform Administrator approves it  
**Then** its status becomes **Available**.

**Given** a listing violates scope or policy  
**When** the Platform Administrator rejects or removes it  
**Then** buyers cannot reserve it.

## AC-04 — Search and comparison (FR-04)

**Given** approved Available listings exist  
**When** a buyer searches or filters by relevant criteria  
**Then** matching listings are displayed with current price, category, seller and availability information.

## AC-05 — Reserve an available listing (FR-05 / UC-05)

**Given** an eligible buyer is viewing an approved **Available** listing  
**When** the buyer confirms the reservation  
**Then** exactly one **Pending** order is created  
**And** the listing changes from **Available** to **Reserved**  
**And** a 24-hour seller-response deadline is recorded  
**And** the seller is notified or the notification is queued/recorded for retry.

**Given** the listing is no longer Available when confirmation is processed  
**When** the system rechecks availability  
**Then** no new order is created  
**And** the current listing state is preserved  
**And** the buyer receives a refusal reason.

**Given** two buyers confirm the same listing at nearly the same time  
**When** both requests are processed  
**Then** only one live reservation succeeds.

## AC-06 — Seller response (FR-06)

**Given** a Pending order  
**When** the seller accepts it  
**Then** the order becomes **Accepted**  
**And** the listing remains **Reserved**.

**Given** a Pending order  
**When** the seller rejects it  
**Then** the order becomes **Rejected**  
**And** the listing returns to **Available**.

## AC-07 — Expiry and cancellation (FR-07)

**Given** a Pending order  
**When** 24 hours pass without seller response  
**Then** the order becomes **Expired**  
**And** the listing returns to **Available**.

**Given** a live order before physical handover  
**When** the buyer cancels  
**Then** the order becomes **Cancelled**  
**And** the listing returns to **Available**.

## AC-08 — Delivery and completion (FR-08)

**Given** an Accepted order and an offline handover has taken place  
**When** the seller records delivery  
**Then** the order becomes **Delivered**.

**Given** a Delivered order  
**When** the buyer confirms receipt  
**Then** the order becomes **Completed**  
**And** the listing becomes **Sold**.

## AC-09 — Reviews (FR-09)

**Given** an order is not Completed  
**When** a review is submitted  
**Then** the review is rejected.

**Given** a Completed order with no existing review  
**When** its buyer submits a review  
**Then** one review is stored and contributes to the seller rating.

**Given** a review already exists for the order  
**When** another review is submitted  
**Then** the second review is rejected.

## AC-10 — Reports and disputes (FR-10)

**Given** a buyer or seller identifies a problem with a listing, user or order  
**When** a report is submitted  
**Then** a Report is stored with status **Open**.

**Given** an Open report  
**When** the Platform Administrator begins review  
**Then** it becomes **Under Review**.

**Given** the issue can be resolved internally  
**When** the administrator records the outcome  
**Then** the report becomes **Resolved**.

**Given** a serious issue remains unresolved  
**When** escalation is required  
**Then** the report becomes **Escalated** and may be referred to the SRC.