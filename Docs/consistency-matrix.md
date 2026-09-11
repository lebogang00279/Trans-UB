TRANS-UB Lab 5 Consistency Matrix

Core workflow


| ID | Requirement | Use-case step / condition | Sequence message | Responsibility / analysis element | State / transition | Verification |
|---|---|---|---|---|---|---|
| CM-01 | FR-01 | Buyer eligibility is checked. | `isEligible()` | `buyer:StudentAccount` | Buyer must be eligible/active. | Invalid or suspended buyer is refused. |
| CM-02 | FR-03, FR-05 | Listing approval/status is checked. | `isReservableBy(buyer)` | `listing:Listing` | Guard: Approved and Available; buyer != seller. | Unapproved, removed, reserved or own listing is refused. |
| CM-03 | FR-05, D-001 | System explains reservation terms. | return `reservation terms` | `:ReserveListingControl` → `:ReserveListingBoundary` | No state change. | Buyer sees 24-hour response and offline payment/handover disclosure. |
| CM-04 | FR-05 | Buyer confirms reservation. | `confirmReserve(note)` | `:ReserveListingBoundary` → `:ReserveListingControl` | Processing begins. | Optional note is accepted. |
| CM-05 | FR-05 | Availability is rechecked at confirmation. | `isReservableBy(buyer)` | `:ReserveListingControl` → `listing:Listing` | Guard: still Available. | Stale listing is refused before Order creation. |
| CM-06 | FR-05 | Order is created. | `create(buyer, listing, note, deadline = now + 24h)` | `order:Order` | Order: none → Pending. | Exactly one Pending order is stored with a 24-hour deadline. |
| CM-07 | FR-05 | First status history entry is created. | `create(none -> Pending)` | `change:OrderStatusChange` | History records Pending. | Status/time/actor type are recorded. |
| CM-08 | FR-05 | Listing is locked for this order. | `reserve(order)` | `listing:Listing` | Listing: Available → Reserved. | Second live reservation cannot succeed. |
| CM-09 | FR-05 | Seller notification is raised. | `raise(new order, seller)` | `notice:Notification` | Order remains Pending. | Notification outcome is recorded. |
| CM-10 | FR-05 | Notification fails. | return `notification result` | Notification + Order | No rollback: Order Pending; Listing Reserved. | Failure is recorded for retry; reservation remains valid. |
| CM-11 | FR-05 | Listing became unavailable before confirmation. | alt branch after second `isReservableBy(buyer)` | Listing + Control | No new Order; Listing keeps current state. | Buyer receives refusal reason/refreshed listing. |

## Follow-on lifecycle consistency

| ID | Requirement | Event | Analysis responsibility | State transition | Verification |
|---|---|---|---|---|---|
| CM-12 | FR-06 | Seller accepts | `Order.accept()` | Pending → Accepted; Listing stays Reserved | Verify Accepted state. |
| CM-13 | FR-06 | Seller rejects | `Order.reject()` + `Listing.release()` | Pending → Rejected; Reserved → Available | Verify release. |
| CM-14 | FR-07 | 24-hour deadline passes | `Order.expire()` + `Listing.release()` | Pending → Expired; Reserved → Available | Verify automatic expiry/release. |
| CM-15 | FR-07 | Buyer cancels before handover | `Order.cancel()` + `Listing.release()` | Pending/Accepted → Cancelled; Reserved → Available | Verify cancellation/release. |
| CM-16 | FR-08 | Seller records handover | `Order.markDelivered()` | Accepted → Delivered | Verify Delivered. |
| CM-17 | FR-08 | Buyer confirms receipt | `Order.confirmReceipt()` + `Listing.markSold()` | Delivered → Completed; Reserved → Sold | Verify completion. |
| CM-18 | FR-09 | Buyer reviews transaction | Review creation | Guard: Order == Completed; Review 0..1 | Reject before completion and reject duplicate review. |
| CM-19 | FR-10 | User submits report | `Report.open()` | Report: new → Open | Verify target/reason/status stored. |
| CM-20 | FR-10 | Administrator starts review | `Report.startReview()` | Open → Under Review | Verify admin review status. |
| CM-21 | FR-10 | Administrator resolves/escalates | `Report.resolve()` / `Report.escalate()` | Under Review → Resolved/Escalated | Verify resolution or SRC escalation is recorded. |

## Agreed Phase 1 state vocabulary

**Order:** Pending, Accepted, Rejected, Expired, Cancelled, Delivered, Completed.  
**Listing:** Pending Approval, Available, Reserved, Sold, Removed.  
**Report:** Open, Under Review, Resolved, Escalated.
