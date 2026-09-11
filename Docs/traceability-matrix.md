 TRANS-UB Traceability Matrix

| Requirement ID | Core requirement | Use case | Analysis element(s) | Verification |
|---|---|---|---|---|
| **FR-01** | Register/login with simulated Student-ID verification. | Register Account; Login | StudentAccount | Test valid/invalid synthetic verification and active/suspended account access. |
| **FR-02** | Create/edit an approved low-risk physical-good listing. | Create Listing; Edit Listing | StudentAccount (seller); Listing | Create/edit valid listing; reject incomplete/prohibited listing from publication. |
| **FR-03** | Approve/reject/remove listings. | Moderate Listing | Platform Administrator; Listing; ListingApproval | Approve a pending listing to Available; reject/remove and verify buyers cannot reserve it. |
| **FR-04** | Search, browse, filter and compare listings. | Search/Browse Listings | StudentAccount (buyer); Listing | Search/filter and verify current matching approved listings are returned. |
| **FR-05** | Reserve/order an Available listing. | **UC-05 Reserve an available listing** | StudentAccount (buyer); Listing; Order; OrderStatusChange; Notification; ReserveListingBoundary; ReserveListingControl | Confirm reservation: one Pending order is created, Listing Available â Reserved, duplicate/live second reservation is refused. |
| **FR-06** | Seller accepts/rejects Pending order. | Respond to Order | StudentAccount (seller); Order; Listing; OrderStatusChange | Accept - Accepted; reject -Rejected and Listing Reserved -Available. |
| **FR-07** | 24-hour expiry and buyer cancellation. | Expire Order; Cancel Order | Order; Listing; OrderStatusChange | No response - Expired; cancellation - Cancelled; Listing returns to Available. |
| **FR-08** | Mark Delivered and confirm receipt. | Mark Delivered; Confirm Receipt | StudentAccount (seller/buyer); Order; Listing; OrderStatusChange | Accepted - Delivered - Completed; Listing becomes Sold. |
| **FR-09** | One review after Completed order. | Submit Review | StudentAccount (buyer/seller); Order; Review | Reject before Completed; accept one after Completed; reject second review. |
| **FR-10** | Report and resolve/escalate issues. | Submit Report; Resolve Report | StudentAccount; Report; Platform Administrator; Listing/Order as target | Report Open - Under Review - Resolved/Escalated; verify resolution/moderation action is recorded. |

## Traceability rule

Every identifier, state name and analysis element in this matrix must use the same terminology as the requirements, glossary, models, consistency matrix and tests.