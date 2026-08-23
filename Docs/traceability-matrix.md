|Requirement ID|Core Requirement                                                                         |Use Case                                      |Analysis Element(s)                           |Verification                                                                                                       |
|:------------:|-----------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|**FR-01**     |Register and log in using simulated Student-ID verification.                             |Register Account; Login                       |Student; Account; Verification                |Test valid and invalid synthetic Student-ID data. Verify that only approved users can log in.                      |
|**FR-02**     |Create and edit listings for approved low-risk physical goods.                           |Create Listing; Edit Listing                  |Seller; Listing; Product                      |Create and edit a listing. Verify saved changes. Test a prohibited item and confirm it is rejected or flagged.     |
|**FR-03**     |Approve or remove listings.                                                              |Moderate Listing                              |Administrator; Listing                        |Submit a listing and verify that an administrator can approve or remove it and update its status.                  |
|**FR-04**     |Search, browse and filter available listings.                                            |Search Listings; Browse Listings              |Buyer; Listing; Catalogue                     |Search by keyword/category and verify that only relevant available listings are shown.                             |
|**FR-05**     |Add an available item to a cart and confirm an order.                                    |Add to Cart; Confirm Order                    |Buyer; Cart; CartItem; Order; Listing         |Add an item to the cart and confirm the order. Verify that an order is created and the item is reserved.           |
|**FR-06**     |Handle reservation expiry, seller rejection, buyer cancellation and seller no-response.  |Manage Reservation; Cancel Order; Reject Order|Order; Reservation; OrderStatus; Buyer; Seller|Test each case and verify the correct order status and release of the reserved item where applicable.              |
|**FR-07**     |Mark an item as delivered after physical handover and allow the buyer to confirm receipt.|Mark Delivered; Confirm Receipt               |Order; Seller; Buyer; OrderStatus             |Mark an order as Delivered, then confirm receipt. Verify that the order changes to Completed.                      |
|**FR-08**     |Mark listings as sold or unavailable.                                                    |Mark Listing Sold; Mark Listing Unavailable   |Seller; Listing                               |Mark a listing sold/unavailable and verify that a buyer can no longer order it.                                    |
|**FR-09**     |Rate or review a seller only after a completed transaction.                              |Submit Rating; Submit Review                  |Buyer; Review; Rating; Order                  |Attempt a review before completion and verify rejection. Complete the order and verify that the review is accepted.|
|**FR-10**     |Report problems or disputes and allow administrators to resolve them.                    |Submit Report; Resolve Dispute                |Report; Dispute; Student; Administrator; Order|Submit a report linked to an order. Verify that an administrator can review, update and resolve it.                |

Traceability Structure

Requirement → Use Case → Analysis Element → Verification

Scope Constraints

• Payments are handled outside the TRANS-UB platform.
• Physical handovers take place outside the platform.
• Only approved low-risk physical goods are included in the prototype.
• Food, medicines, alcohol, stolen property, restricted products and high-risk services are excluded.
• Student-ID verification uses synthetic data and is not connected to official University of Botswana records.