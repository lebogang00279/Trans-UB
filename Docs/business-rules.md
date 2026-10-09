                                            Business Rules & Variants
                                            

| ID | Business rule |
|---|---|
| **BR-01 — Student identity** | Protected buyer and seller actions require a prototype account that has passed simulated student verification and is active. |
| **BR-02 — Allowed listings** | Only approved low-risk physical goods may be published. Food, medicines, alcohol, stolen property, restricted products and high-risk services are prohibited in the prototype. |
| **BR-03 — Listing approval** | A listing must be approved before it can enter the **Available** state. |
| **BR-04 — Reservation lock** | A successful buyer confirmation immediately creates exactly one **Pending** order and changes the listing from **Available** to **Reserved**. A listing must never remain Reserved without a matching live order. |
| **BR-05 — No duplicate live reservation** | At most one order for a listing may be in a live reservation state at a time. A second buyer confirming the same listing must be refused once the first reservation succeeds. |
| **BR-06 — Seller response** | The seller may accept or reject a Pending order. Rejection changes the order to **Rejected** and releases the listing to **Available**. |
| **BR-07 — Expiry and cancellation** | A Pending order expires after 24 hours without seller response. A buyer may cancel before physical handover. Expiry or cancellation releases the listing to **Available**. |
| **BR-08 — Completion sequence** | An order cannot become **Completed** until it has first become **Delivered**. Successful completion changes the listing to **Sold**. |
| **BR-09 — Review restriction** | Only the buyer of a Completed order may submit a review, and each order may have at most one review. |
| **BR-10 — Offline payment and handover** | TRANS-UB does not process or hold money and does not perform physical handover. These activities occur directly between buyer and seller. |
| **BR-11 — Reporting** | Buyers and sellers may submit reports. The Platform Administrator records the resolution or escalation. Serious unresolved disputes may be escalated to the SRC. |
| **BR-12 — Notification failure** | Failure to deliver a seller notification does not roll back a successfully created reservation. The notification outcome must be recorded for retry or later visibility. |
