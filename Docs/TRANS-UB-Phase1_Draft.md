**UNIVERSITY OF BOTSWANA**

**CSI473 - Software Design and Architecture**

**CSI473 Project Design Report**

**TRANS-UB - University of Botswana Student Marketplace Hub**

**Team 9 | Phase 1 Draft**

| **Field**              | **Complete**                                                                                                                                                               |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Assignment/phase       | Phase 1 Draft                                                                                                                                                              |
| Approved project title | TRANS-UB - University of Botswana Student Marketplace Hub                                                                                                                  |
| Approval decision/date | Approved with minor conditions; decision date to be confirmed                                                                                                              |
| Team number            | 9                                                                                                                                                                          |
| Members and IDs        | Letlhabile Xoliso Serufo - 202302072 <br>Lebogang Rantlheng - 202400279 <br>Tshegofatso Botho Wakwena - 202302811 <br>Amanda Mapete - 202303699 <br>Lame Vambu - 202203427 |
| Repository URL         | <https://github.com/lebogang00279/Trans-UB>                                                                                                                                |
| Submission tag         | Phase 1 draft - tag to be added before submission                                                                                                                          |
| Date                   | 8 September 2026                                                                                                                                                           |

# 1\. Executive summary

TRANS-UB is a proposed student-to-student marketplace for the University of Botswana. The project responds to the current situation in which student trading is spread across WhatsApp groups, Facebook posts, notice boards and word of mouth, making it difficult for buyers to compare offers and for reliable sellers to build a visible reputation. Phase 1 defines the approved problem, scope, requirements, quality scenarios, domain responsibilities and the core order/reservation lifecycle.

The first implementation is deliberately restricted to low-risk physical goods. Food, medicines, alcohol, stolen property, restricted products and high-risk services are outside the prototype scope. Student-ID verification is simulated using synthetic test data and is not integrated with official University of Botswana records.

A major design boundary is Decision D-001: TRANS-UB records orders and transaction status but does not process payments or perform the physical handover. Payment and handover are arranged directly between the buyer and seller. The key end-to-end workflow is therefore: verified buyer finds an available listing, reserves it, seller accepts or rejects, the parties meet offline, seller marks Delivered, buyer confirms receipt, the order becomes Completed, and only then may the buyer submit one review for that transaction.

This draft is based on the current repository artefacts and highlights the remaining Phase 1 work: finalising the analysis/domain model, producing the sequence and state-machine models, reconciling older cart wording, and ensuring the same requirement IDs, state names and responsibilities are used consistently across all artefacts.

# 2\. Problem evidence, stakeholders and scope

## 2.1 Problem statement and evidence

Students at the University of Botswana already buy and sell items informally, but the market is fragmented across multiple communication channels. Listings become buried, buyers cannot easily compare sellers or prices, and there is little persistent evidence of previous successful transactions. The project evidence currently includes screenshots of student buy-and-sell activity, sampled Facebook advertising and interviews with five student sellers and five student buyers.

| **Evidence/source**                    | **Origin**                 | **What it indicates**                                                                                    |
| -------------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------- |
| Student buy-and-sell group screenshots | Collected 7 Aug 2026       | Active trading exists, but listings have little structure, verification or persistent seller identity.   |
| Interviews with 5 sellers and 5 buyers | UB main campus, 7 Aug 2026 | Sellers reported visibility/trust problems; buyers reported uncertainty about safe and reliable sellers. |
| Facebook sales posts                   | Sampled 7 Aug 2026         | Offers and prices are spread across separate posts, making comparison difficult.                         |

## 2.2 Goal and objectives

Goal: Design and build a central online marketplace where verified UB students can list and find approved goods, compare offers, create transaction records and build seller reputation from confirmed transactions.

- Provide one searchable catalogue of approved student listings organised by useful criteria such as category and price.
- Allow buyers to compare available listings before reserving or ordering.
- Improve trust through simulated student verification, transaction-linked reviews and administrative moderation.

## 2.3 Stakeholders

| **Stakeholder**        | **Main need**                                      | **Main concern**                                         |
| ---------------------- | -------------------------------------------------- | -------------------------------------------------------- |
| Student Seller         | Reach student buyers and manage own listings.      | Trust, visibility and fair handling of orders.           |
| Student Buyer          | Find, compare and reserve suitable listings.       | Scams, stale listings and unreliable sellers.            |
| Platform Administrator | Approve listings and handle reports.               | Consistent moderation and prohibited-item control.       |
| SRC                    | Oversight/escalation interest in serious disputes. | Fraud, prohibited goods and unresolved student disputes. |
| University Management  | Safety and reputational oversight.                 | Risk and liability associated with campus trading.       |

## 2.4 Approval conditions and scope boundary

- First implementation is limited to approved low-risk physical goods.
- Food, medicines, alcohol, stolen property, restricted products and high-risk services are excluded from the prototype.
- Listing approval, reservation expiry, seller rejection, buyer cancellation, seller no-response, reporting and dispute-handling rules must be defined.
- Payments and physical handovers remain outside TRANS-UB; public campus handover locations should be recommended.
- Student-ID verification is simulated using synthetic data and must not be presented as official UB integration.

| **In scope**                                                        | **Out of scope**                                          |
| ------------------------------------------------------------------- | --------------------------------------------------------- |
| Prototype registration/login with simulated student-ID verification | Live integration with UB student records or login systems |
| Seller listing creation/editing for approved low-risk goods         | Online payment processing or escrow                       |
| Administrator approval/rejection/removal of listings                | Delivery/logistics tracking                               |
| Search, browse, filter and compare listings                         | Automated fraud detection                                 |
| Reservation/order lifecycle and transaction status history          | Native mobile application                                 |
| Completed-transaction reviews and reporting/dispute handling        | High-risk or prohibited product/service categories        |

## 2.5 Assumptions and constraints

- The prototype uses fabricated or anonymised accounts, listings and orders for testing.
- Users have access to a smartphone or laboratory computer and normal campus internet.
- The semester schedule, a five-person team and free-tool/hosting constraints limit the amount of functionality that can be implemented.
- A listing represents a single low-risk item in the first prototype; inventory management is not required.
- The SRC has not yet been formally consulted, so escalation details remain a stakeholder-validation item.

# 3\. Glossary

| **Term**               | **Definition**                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| TRANS-UB               | Student marketplace prototype for listing, finding, reserving and recording transactions for approved goods. |
| Student Buyer          | Verified prototype account that searches, compares, reserves items, confirms receipt and may submit reviews. |
| Student Seller         | Verified prototype account that creates listings, responds to orders and records delivery.                   |
| Listing                | A seller's low-risk physical item offered through TRANS-UB.                                                  |
| Available              | Listing state in which a buyer may reserve/order the item.                                                   |
| Reserved               | Listing state in which an active order prevents another buyer from ordering the same item.                   |
| Order                  | Transaction record linking one buyer, one seller and one listing.                                            |
| Pending                | Order awaiting the seller's response.                                                                        |
| Accepted               | Order accepted by the seller and awaiting physical handover.                                                 |
| Delivered              | Seller-recorded state indicating that the offline handover has taken place.                                  |
| Completed              | Buyer-confirmed state indicating receipt; enables review eligibility.                                        |
| Review                 | One rating/comment linked to a Completed order.                                                              |
| Report                 | A user-raised issue against a listing, user or order for administrator handling.                             |
| Platform Administrator | Role that approves/removes listings, handles reports and may suspend accounts.                               |
| Synthetic verification | Prototype check using fabricated test data rather than official UB systems.                                  |

# 4\. Functional requirements and use cases

## 4.1 Functional requirements

| **ID** | **Requirement**        | **Phase 1 statement**                                                                                                                                        |
| ------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| FR-01  | Registration and login | Allow students to register and log in using prototype accounts with student-ID verification simulated using synthetic test data.                             |
| FR-02  | Create/edit listing    | Allow a seller to create and edit a listing for an approved low-risk physical good.                                                                          |
| FR-03  | Listing approval       | Allow the administrator to approve, reject or remove listings before buyers can use them.                                                                    |
| FR-04  | Search/browse          | Allow buyers to search, browse, filter and compare approved listings by criteria such as category, price and seller rating.                                  |
| FR-05  | Reserve/order          | Allow a buyer to reserve/order an Available listing and change it to Reserved to prevent simultaneous ordering.                                              |
| FR-06  | Seller response        | Allow the seller to accept or reject a Pending order; rejection returns the listing to Available.                                                            |
| FR-07  | Expiry/cancellation    | Automatically expire an unanswered order after 24 hours and allow buyer cancellation before handover; release the listing in either case.                    |
| FR-08  | Confirm completion     | Allow seller to mark Delivered and buyer to confirm receipt, changing the order to Completed.                                                                |
| FR-09  | Ratings/reviews        | Allow one review only from a buyer with a Completed order and recalculate seller rating from completed-transaction reviews.                                  |
| FR-10  | Reporting/disputes     | Allow buyers/sellers to report a listing, user or order; allow the administrator to resolve, remove, suspend or escalate serious unresolved disputes to SRC. |

## 4.2 Actors and actor goals

- Student Buyer: find trustworthy items, compare listings, reserve/order an item, confirm receipt, review completed transactions and raise reports.
- Student Seller: create/manage approved listings, respond to pending orders, arrange offline handover, mark delivery and build transaction-backed reputation.
- Platform Administrator: approve/remove listings, review reports, suspend accounts where allowed and record/escalate dispute outcomes.

## 4.3 Use-case model

Editable source: Models/usecasemodel.drawio. Readable export: Models/usecasemodel.svg.

The current use-case model should be treated as a Phase 1 artefact and checked against FR-01 to FR-10. In particular, the order workflow must use the same terminology as the detailed UC-05 and the lifecycle model.

## 4.4 Core detailed use case - UC-05 Reserve an available listing

| **Use case**            | **UC-05 - Reserve an available listing**                                                                                            |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Primary actor**       | Student Buyer                                                                                                                       |
| **Goal**                | Secure an available listing and create a Pending transaction record without allowing duplicate reservation.                         |
| **Preconditions**       | Buyer is authenticated/eligible; listing is approved and Available; buyer is not the seller.                                        |
| **Trigger**             | Buyer chooses to reserve/order an available listing.                                                                                |
| **Main success result** | Exactly one Pending order is created and the listing changes Available -> Reserved; a 24-hour seller-response deadline is recorded. |
| **Seller response**     | Seller may Accept (order becomes Accepted) or Reject (order becomes Rejected and listing returns to Available).                     |
| **Exceptions**          | Stale/unavailable listing; duplicate submission; simultaneous reservation; storage failure; notification failure.                   |
| **Postcondition**       | Buyer and seller can see the active order; payment and physical handover remain outside TRANS-UB.                                   |

## 4.5 Acceptance criteria summary

- Given an authenticated eligible buyer and an approved Available listing, when the buyer confirms reservation, then exactly one Pending order is created and the listing becomes Reserved.
- If the listing is no longer Available at confirmation time, no order is created and the buyer receives a clear failure reason.
- If two buyers attempt to reserve the same listing concurrently, only one reservation succeeds.
- If seller rejects or the 24-hour response period expires, the order reaches the appropriate terminal state and the listing returns to Available.
- A review is rejected unless the linked order is Completed, and no more than one review is permitted per completed transaction.

# 5\. Quality requirements

The repository defines measurable quality scenarios. The Phase 1 design must show which responsibilities and data/state rules make these scenarios achievable.

| **Quality requirement**        | **Measure**                                                                         | **Design obligation**                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| QR-01 Search performance       | Relevant search results visible within 2 seconds for at least 95% of searches.      | Keep search/filter operations simple and index searchable listing fields in the eventual data design.   |
| QR-02 Listing performance      | Listing details displayed within 2 seconds for at least 95% of requests.            | Separate listing retrieval from slower optional operations and avoid unnecessary external dependencies. |
| QR-03 Access control           | 100% of listing attempts by unverified users are rejected.                          | Verification/authorization guard before seller listing actions.                                         |
| QR-04 Listing validation       | 100% of incomplete listings are rejected before publication.                        | Central listing validation and administrator moderation.                                                |
| QR-05 Order reliability        | 99% of valid order confirmations complete within 3 seconds without data loss.       | Atomic order creation + listing state update.                                                           |
| QR-06 Duplicate prevention     | Zero duplicate orders from repeated identical submissions.                          | Idempotency/duplicate check and unique active reservation rule.                                         |
| QR-07 Listing update integrity | 100% of valid updates affect only the intended seller's listing.                    | Ownership check on update operation.                                                                    |
| QR-08 Review integrity         | 100% of reviews for non-completed transactions are rejected.                        | Completed-order guard and one-review-per-order constraint.                                              |
| QR-09 Stale listing conflict   | 100% of orders based on unavailable/stale listing state are rejected or reconciled. | Re-check current listing state at confirmation and use atomic reservation.                              |

Note: the existing scenario describing an external messaging service should be reconciled with the approved design. The current core workflow only requires reliable visibility/notification of a Pending order; an external messaging integration should not be assumed unless it becomes an explicit design element.

# 6\. Analysis/domain model and responsibilities

A formal domain-model diagram is still a Phase 1 deliverable. The responsibility allocation below provides the working analysis model that the diagram should reflect.

| **Analysis element**                  | **Main responsibility**                                                                                                     |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| StudentAccount                        | Maintain prototype identity, verification state, role eligibility and account status.                                       |
| Listing                               | Store item description, category, price, seller and lifecycle status; enforce Available/Reserved/Sold-or-Unavailable rules. |
| Order                                 | Link one buyer, seller and listing; maintain lifecycle state, response deadline and status history.                         |
| Review                                | Store one rating/comment for one Completed order and support seller-rating calculation.                                     |
| Report                                | Record reported target, reason, status and administrator resolution/escalation.                                             |
| Administrator                         | Approve/reject/remove listings; review reports; suspend accounts; record moderation actions.                                |
| TRANS-UB application/controller layer | Coordinate use-case steps, validation, atomic reservation, authorization and user feedback.                                 |

## 6.1 Business rules

| **Rule** | **Statement**                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------ |
| BR-01    | Only prototype accounts that pass simulated student verification may perform protected buyer/seller actions. |
| BR-02    | Only approved low-risk physical goods may be published; prohibited categories remain outside the prototype.  |
| BR-03    | A listing must be Available at the instant a reservation is confirmed.                                       |
| BR-04    | A successful reservation immediately changes Available -> Reserved and creates exactly one Pending order.    |
| BR-05    | Seller rejection, buyer cancellation or 24-hour no-response releases the listing back to Available.          |
| BR-06    | Payment and physical handover occur outside TRANS-UB; the platform only records transaction states.          |
| BR-07    | Only a Completed order enables one review for that transaction.                                              |
| BR-08    | Reports are handled by the administrator; serious unresolved disputes may be escalated to SRC.               |

## 6.2 Responsibility rationale

The design keeps business state in domain records such as Listing, Order, Review and Report, while use-case coordination belongs to the application/controller layer. This avoids placing reservation, verification and moderation logic inside user-interface screens. The Order and Listing must be updated together for reservation because FR-05 and the duplicate-prevention quality requirement depend on a single consistent state change.

# 7\. Interaction and lifecycle

Phase 1 interaction/lifecycle modelling is centred on UC-05 because it creates the transaction record used by seller response, completion, review and dispute handling.

## 7.1 Core interaction sequence

1. Buyer requests reservation for an approved listing.
2. System validates buyer eligibility and confirms that the listing is still Available.
3. System presents reservation terms, including 24-hour seller response and the offline payment/handover boundary.
4. Buyer confirms the reservation.
5. System atomically creates a Pending Order and changes the Listing from Available to Reserved.
6. System records the response deadline/status history and makes the Pending order visible to the seller.
7. Seller accepts or rejects. Rejection returns the Listing to Available.
8. If accepted, physical handover occurs outside TRANS-UB; seller records Delivered and buyer confirms receipt to reach Completed.
9. Only after Completed may the buyer submit one Review.

Planned editable/readable model files: Models/sequence-core-use-case.\* and Models/state-machine.\*. These should be committed before Phase 1 submission.

## 7.2 State model

Working order lifecycle:

**Pending -> Accepted -> Delivered -> Completed**

- Pending -> Rejected
- Pending -> Expired (seller no-response after 24 hours)
- Pending -> Cancelled
- Accepted -> Cancelled before physical handover, if the agreed rule permits it

Working listing lifecycle:

**Pending Approval -> Available -> Reserved -> Sold/Unavailable**

Reserved returns to Available when the associated order is Rejected, Expired or Cancelled.

## 7.3 Consistency explanation

The consistency matrix should link each core use-case step to a sequence message, responsible analysis element, requirement and state transition. For example, FR-05 maps to UC-05 reservation confirmation, createOrder(...), Listing/Order responsibilities, the transitions Order -> Pending and Listing Available -> Reserved, and verification that only one active reservation exists. The same labels must be used in the use case, sequence diagram, state machine, requirements file and tests.

# 8\. Architecture and decisions

Phase 2 detail. Phase 1 records Decision D-001 as the confirmed boundary: no online payment and no platform-controlled physical handover. Component alternatives and the full architecture model are still to be completed.

# 9\. Data, API/service and deployment design

Phase 2 detail. Phase 1 identifies the core records StudentAccount, Listing, Order, Review and Report. Logical schema, API contracts and deployment design remain to be completed.

# 10\. Detailed design, patterns and framework

Phase 2 detail. Interfaces/classes, selected patterns, rejected pattern alternatives and framework boundaries are not yet finalised.

# 11\. User-interface, accessibility and usability

Phase 2 detail. Task flows and wireframes should include success, empty, validation, stale-listing and permission-denied states, with accessibility evidence.

# 12\. Implementation vertical slice

The approved vertical slice is the reservation/order-to-completion path centred on UC-05. Prototype implementation and run instructions are Phase 2 deliverables.

# 13\. Testing and results

Phase 1 has defined requirement-linked verification intentions. Executed automated/manual test results and quality evidence are Phase 2 deliverables.

# 14\. Reconciliation and change history

The repository currently contains older wording in some artefacts, especially cart-based ordering and earlier state names such as 'Pending handoff'. Before Phase 1 submission, the team should reconcile these with the authoritative FR-05 to FR-08 workflow: reserve -> Pending -> Accepted/Rejected -> Delivered -> Completed, including Expired/Cancelled paths. The traceability and consistency matrices should be updated after every terminology or lifecycle change.

| **Issue**                                               | **Required reconciliation**                                                        | **Affected artefacts**                                     |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Cart wording remains in older scope/acceptance material | Either formally adopt a cart or remove it from Phase 1 core workflow.              | problem-and-scope.md; acceptance-criteria.md; glossary.md  |
| Earlier order state names differ                        | Standardise Pending, Accepted, Rejected, Expired, Cancelled, Delivered, Completed. | requirements; glossary; use cases; state/sequence diagrams |
| Listing state after completed sale                      | Agree and use one final terminal label such as Sold or Unavailable.                | glossary; domain/state model; tests                        |
| Messaging scenario assumes an external service          | Remove or explicitly design that dependency.                                       | quality scenarios; sequence/architecture models            |

# 15\. Risks, technical debt and release recommendation

| **Risk / debt**              | **Current control**                                | **Phase 1 recommendation**                                                |
| ---------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------- |
| Unauthorised or fake users   | Synthetic verification and account suspension rule | Keep test data synthetic; do not imply live UB integration.               |
| Prohibited/stolen goods      | Low-risk scope, approval and reporting             | Maintain explicit prohibited-category validation and moderation evidence. |
| Duplicate/stale reservations | Available/Reserved lifecycle                       | Model and later implement atomic reservation plus duplicate check.        |
| Offline transaction safety   | D-001 boundary and status recording                | Display clear boundary and recommend public campus handover points.       |
| Privacy                      | Synthetic data and limited personal data           | Keep prototype database non-public and hash passwords in implementation.  |
| Model inconsistency          | Traceability/consistency matrices                  | Resolve naming conflicts before tagging Phase 1.                          |

Phase 1 release recommendation: suitable for submission after the sequence model, state-machine/activity model and reconciled consistency matrix are committed and the remaining terminology conflicts are closed.

# 16\. Academic integrity and AI-use record

Draft disclosure: generative AI assistance was used to help organise the report, review cross-artefact consistency and draft explanatory text. The team remains responsible for checking every requirement, diagram, decision, test and repository reference against the approved project scope and for editing the final report into the team's own verified work. Any course-required AI-use declaration should be completed according to the lecturer's rules.

# References

1. University of Botswana. CSI473 Project Design Report Template, Semester 1, 2026/27.
2. TRANS-UB repository: Docs/project-proposal-and-approval.md.
3. TRANS-UB repository: Docs/problem-and-scope.md.
4. TRANS-UB repository: Docs/requirements.md.
5. TRANS-UB repository: Docs/stakeholders.md.
6. TRANS-UB repository: Docs/SCENARIOS MD.md.
7. TRANS-UB repository: Glossary/glossary.md.
8. TRANS-UB repository: Decisions/D-001.md.
9. TRANS-UB repository: Models/usecasemodel.drawio and Models/usecasemodel.svg.
10. TRANS-UB repository: Docs/traceability-matrix.md and Docs/consistency-matrix.md (when committed).

# Appendices

## Appendix A - Phase 1 artefact checklist

| **Artefact**              | **Repository location**               | **Status**                                                  |
| ------------------------- | ------------------------------------- | ----------------------------------------------------------- |
| Project proposal/approval | Docs/project-proposal-and-approval.md | Present                                                     |
| Problem and scope         | Docs/problem-and-scope.md             | Present; needs reconciliation with current no-cart workflow |
| Requirements              | Docs/requirements.md                  | Present                                                     |
| Stakeholders              | Docs/stakeholders.md                  | Present                                                     |
| Glossary                  | Glossary/glossary.md                  | Present; needs state terminology update                     |
| Use-case model            | Models/usecasemodel.drawio + .svg     | Present                                                     |
| Detailed core use case    | Docs/use-case/...UC05...md            | Present                                                     |
| Traceability matrix       | Docs/traceability-matrix.md           | Present; verify IDs against requirements                    |
| Consistency matrix        | Docs/consistency-matrix.md            | To be committed                                             |
| Core sequence model       | Models/sequence-core-use-case.\*      | Pending                                                     |
| State/activity model      | Models/state-machine.\*               | Pending                                                     |

## Appendix B - Initial traceability summary

| **Req.** | **Use case**        | **Analysis elements**        | **Verification**                                  |
| -------- | ------------------- | ---------------------------- | ------------------------------------------------- |
| FR-01    | Register/Login      | StudentAccount, verification | Valid/invalid synthetic-ID and access tests       |
| FR-02    | Create/Edit Listing | Seller, Listing              | Create/update and prohibited-item validation      |
| FR-03    | Moderate Listing    | Administrator, Listing       | Approve/reject/remove status tests                |
| FR-04    | Search/Browse       | Buyer, Listing catalogue     | Keyword/filter/availability tests                 |
| FR-05    | Reserve/Order       | Buyer, Order, Listing        | Pending order + Available->Reserved; no duplicate |
| FR-06    | Accept/Reject       | Seller, Order, Listing       | Accepted path; Rejected + release listing         |
| FR-07    | Expire/Cancel       | Order, Listing               | 24-hour expiry/cancel + release listing           |
| FR-08    | Delivered/Receipt   | Seller, Buyer, Order         | Accepted->Delivered->Completed                    |
| FR-09    | Review              | Buyer, Review, Order         | Reject before Completed; one review after         |
| FR-10    | Report/Resolve      | User, Report, Administrator  | Create report; resolve/escalate/moderate          |