# TRANS-UB — Consistency Findings (artefacts up to Lab 4)

I read every document produced before Lab 5 against every other one and wrote down where they disagree.

**In scope:** project-proposal-and-approval.md, problem-and-scope.md, stakeholders.md, problem-evidence.md, requirements.md, business-rules.md, acceptance-criteria.md, actor-and-actor-goals.md, traceability-matrix.md, SCENARIOS MD.md, UC-05, D-001, glossary.md, system-context, usecasemodel, crc_cards, domain-model.

**Not in scope:** anything Lab 5 asks the team to produce. I have not treated the sequence model, the lifecycle model, the consistency matrix, the Phase 1 draft or the peer review as missing, and I have not used the sequence model as evidence against anything.

Nothing in the repository has been changed. Every item below needs a team decision.

---

## Blocking. Two documents state opposite things, or the same id means two things

### 1. FR numbers mean different requirements in different documents

`requirements.md` numbers its items 1 to 10. `traceability-matrix.md` numbers FR-01 to FR-10. They agree for the first four and then drift, because the matrix merges two requirements into FR-06 and adds one requirements.md does not have.

| ID | requirements.md | traceability-matrix.md | UC-05 uses it as |
|---|---|---|---|
| 05 | Reserve or order an item | Add an item to a **cart** and confirm an order | Reserve or order an item |
| 06 | Accept or reject orders | Expiry, rejection, cancellation, no-response | Accept or reject orders |
| 07 | Reservation expiry and cancellation | Mark delivered and confirm receipt | Expiry and cancellation |
| 08 | Confirm transaction completion | Mark listings sold or unavailable | Confirm transaction completion |

UC-05 and requirements.md agree with each other. The matrix is the odd one out from FR-05 down, so anyone following FR-07 out of UC-05 lands on the wrong requirement.

Matrix FR-08, mark a listing sold or unavailable, is not in requirements.md at all. It only exists in the in-scope table of problem-and-scope.md.

### 2. requirements.md item 1 holds two requirements and item 2 repeats one of them

Item 1 is "User registration and login", then a second sentence beginning "Create and manage listings" is attached to the same number. Item 2 is then "The system shall allow a seller to create and edit a listing". So the create-listing requirement is in the file twice and item 1 covers two unrelated things. This is almost certainly what caused finding 1.

### 3. Is there a cart or not

| Has a cart | Has no cart |
|---|---|
| proposal section 6, steps 3 and 8 | requirements.md item 5, the buyer reserves a listing directly |
| problem-and-scope in-scope table, "Cart and order confirmation" | UC-05, written without one and listing it as an open issue |
| traceability-matrix FR-05, analysis elements Cart and CartItem | domain-model.md, Cart rejected as an interface term |
| acceptance-criteria scenarios 6, 7 and 8 | crc_cards.svg, no Cart card |
| glossary, an Order is "the record created when a buyer confirms a cart" | usecasemodel, the buyer use case is "Place order", no cart use case |

This has to be settled first, because it moves FR-05, UC-05, the domain model, the glossary and four acceptance scenarios.

### 4. A listing becomes Reserved at three different moments

- `acceptance-criteria.md` scenario 6: the buyer adds the item to the cart and "the listing is reserved". No order exists yet.
- `requirements.md` item 5: the buyer reserves or orders, and the system changes the listing to Reserved to stop a simultaneous order.
- `business-rules.md`, Reservation Window: "An item is not officially reserved for a buyer until the seller approves the request. Up until that point, other users can still ask to buy it."

These cannot all hold. The third deliberately allows several buyers to queue on one listing, which is exactly what requirements.md item 5 is written to prevent, and it contradicts UC-05 success guarantee 2.

The business-rules Stock Lockout item is the same disagreement from another angle, since it assumes several pending order requests can exist against one listing.

Scenario 6 also breaks the UC-05 minimal guarantee, which says the system never leaves a listing Reserved with no matching order behind it.

### 5. The order states have no agreed list

| Document | States it names |
|---|---|
| glossary.md | Pending handoff, Delivered, Completed, Cancelled |
| proposal sections 6 and 7 | Pending handoff, Delivered, Completed, Cancelled |
| requirements.md | Pending, Rejected, Expired, Cancelled, Delivered, Completed |
| UC-05 | Pending, Accepted, Rejected, Expired, Cancelled, Delivered, Completed |
| acceptance-criteria scenario 7 | **Awaiting Collection** |
| acceptance-criteria scenario 9 | Pending handoff |

"Awaiting Collection" appears nowhere else in the project, and acceptance-criteria uses two different names for what looks like one state in scenarios 7 and 9. The glossary, which should be the authority, is missing Accepted, Rejected and Expired even though requirements items 6 and 7 need them.

The listing states have the same problem: the glossary lists Available, Reserved, Sold and Unavailable with no Pending Approval, even though item 3 and UC-05 both depend on Pending Approval existing.

### 6. Three different sets of use case names

The use case model, the traceability matrix and UC-05 name the use cases three different ways, and almost none of them match.

| usecasemodel.drawio | traceability-matrix.md | UC-05 |
|---|---|---|
| Search items | Search Listings; Browse Listings | (trigger only) |
| Place order | Add to Cart; Confirm Order | **Reserve an available listing** |
| Manage listings | Create Listing; Edit Listing | |
| Manage listing approvals | Moderate Listing | |
| Manage order fulfillment | Mark Delivered; Confirm Receipt; Reject Order | |
| Leave and see reviews | Submit Rating; Submit Review | |
| User authentication | Register Account; Login | |
| View reports, Review flagged content | Submit Report | |
| Resolve disputes | Resolve Dispute | |

The only pair that matches is Resolve Dispute. The one fully dressed use case in the project, UC-05, has a name that appears in neither the diagram nor the matrix.

---

## High. Real design disagreements

### 7. University Management is an actor on the use case model and has no system access anywhere else

The `.drawio` source has a direct association from **University management** to the use case **Enforce policies**. That makes it a system user.

- `stakeholders.md`: "Indirect stakeholder, treated through our policy and moderation rules" and it is listed under "Indirect/oversight stakeholders: SRC and University Management do not use the system day to day".
- `system-context.md`: "University Management | — | Policy and liability interest only (shown as a dashed association, no data flow)".
- `actor-and-actor-goals.md`: "Indirect institutional stakeholder".

Three documents say no access, the use case model gives it a use case. There is also no requirement anywhere for an Enforce policies feature.

### 8. Who resolves disputes

- `requirements.md` item 10: the **platform administrator** reviews the report, records a resolution, and escalates serious unresolved disputes to the SRC.
- `usecasemodel`: **Resolve disputes** sits next to the SRC.
- `actor-and-actor-goals.md`: the SRC's goal is to "Receive and handle serious, unresolved dispute escalations", and the administrator's is to "conduct dispute reviews" and "escalate serious unresolved cases".

The requirement and the actor-goals document agree that the administrator resolves and the SRC receives escalations. The use case model reads as though the SRC resolves. Since the SRC has no interface anywhere in the requirements, this matters.

### 9. Five use cases on the diagram have no requirement behind them

Enforce policies, View usage summaries, Generate Performance Metrics, Make notifications and alerts, and View buyer contact do not correspond to anything in requirements.md.

Two of them are worth a decision rather than just deletion. "Make notifications and alerts" is real behaviour the system context already shows ("New order alert"), so it may be a missing requirement rather than a stray use case. "View buyer contact" is the contact-detail rule from the proposal risk table, which is finding 14 below. "Generate Performance Metrics" appears nowhere else in the project at all.

### 10. Two requirements have no use case on the diagram

Item 7, reservation expiry and buyer cancellation, and item 8, mark delivered and confirm receipt, have no use case of their own. "Manage order fulfillment" is broad enough to be hiding several requirements inside one bubble, and it is a seller use case, so the buyer's cancel and confirm-receipt goals are not on the diagram at all.

### 11. The platform coordinates handover, or it does not

`acceptance-criteria.md` scenarios 9 and 10 have the seller entering a campus location and time, clicking "Send Handoff Details", and the buyer clicking "Confirm Meetup", with the meeting shown on both dashboards. `crc_cards.svg` gives the Order card a "Handover instructions" responsibility, which agrees with those scenarios.

`D-001` says handover is arranged offline, outside the platform. `problem-and-scope.md` lists delivery and logistics tracking as out of scope. The domain model rejected Handover as a class for that reason.

Scenarios 9 and 10 are a feature nobody decided to add, sitting against a ratified decision.

### 12. Verification checks a student email in some documents and a student ID in others

- Student **ID**: requirements item 1, glossary, proposal objective 3 and section 8, UC-05 precondition 1, traceability FR-01.
- Student **email**: business-rules Student Identity Check, acceptance-criteria scenarios 1, 2 and 3.

These are different checks. The traceability matrix even specifies the test as "valid and invalid synthetic Student-ID data", which would not exercise what business-rules describes.

### 13. Are buyer and seller separate accounts or two roles of one account

`acceptance-criteria.md` scenarios 1 and 2 have the user choose "Seller" or "Buyer" at registration and receive a different profile and dashboard. Seller registration also collects a shop name and a category.

The domain model treats buyer and seller as roles of one StudentAccount, because the same student sells a textbook this week and buys one next week. UC-05 precondition 5, "the buyer is not the seller of the listing", only makes sense if one account could be both. The CRC cards put Seller and Buyer under a shared User card, which is closer to the roles reading.

If registration forces the choice, a student seller can never buy anything, which is not the world the problem statement describes.

Related: "shop name" and "category of goods or services" appear only in acceptance-criteria. There is no Shop concept in the glossary, the CRC cards or the domain model.

### 14. The traceability matrix names analysis elements that do not exist in the domain model or the CRC cards

The matrix lists Student, Account, Verification, Seller, Product, Buyer, Catalogue, Cart, CartItem, Reservation, OrderStatus, Rating, Dispute. The domain model has StudentAccount, Listing, ListingApproval, Order, OrderStatusChange, Notification, Review. The CRC set has User, Seller, Buyer, Administrator, Listing, Order, Review, Report.

Specific clashes: Product and Listing are one thing under two names; Catalogue and Cart were both rejected as views rather than concepts; Rating, Verification and OrderStatus are attributes rather than classes; Reservation and Order are the same thing; Student and Account are one class. ListingApproval and OrderStatusChange appear in no row of the matrix even though item 3 and the audit rule in UC-05 need them.

### 15. UC-05 cites a version of the proposal that is not in the repository

UC-05 refers to "section 6" for the reservation, expiry, rejection and cancellation rules, "section 7" for the failure to test, and "section 8" for the list of states. In the committed proposal, section 6 is the core workflow, section 7 is the design-suitability check and section 8 is the risk table. None contains what UC-05 says it contains. The failure test UC-05 puts in section 7 is actually section 6 item 8.

UC-05 also traces to "Objective 4, clear rules so each transaction has a clear status". The proposal has three objectives.

Either the revised proposal never reached the repository, or UC-05's references need correcting against the one that did.

---

## Medium

### 16. Services are in the goal and out of the requirements

The problem statement and the goal promise goods **and services**, naming printing, braiding and nail work. The glossary defines a Listing as "a single item or service". Acceptance-criteria asks a seller for a "category of goods or services".

requirements.md item 2, UC-05 precondition 4 and the traceability scope constraints restrict the prototype to approved low-risk **physical goods**, with high-risk services excluded. The same applies to food, which the problem statement names as a thing students sell and UC-05 says can never reach an approved state.

This may be a deliberate narrowing, but no document says so, so the goal currently promises what the requirements refuse to deliver.

### 17. SCENARIOS MD.md calls the system "Student Hub"

Eight of the ten quality scenarios say "Student Hub" rather than TRANS-UB. The proposal's own design-suitability check answers "Not the University Service Hub or a renamed copy: Yes", and a sibling document calling the system a Hub undercuts that answer. Cheapest item on this list to fix and the riskiest to leave.

### 18. Quality scenario 7 assumes an in-app messaging feature

Scenario 7 is about a buyer sending a message to a seller while an external messaging service is down. There is no messaging requirement, no messaging use case, and no messaging entity on the system context diagram. Either messaging is a missing requirement or scenario 7 should be about the new-order alert, which is what the context diagram actually shows.

### 19. Acceptance-criteria scenario 5 adds a feature nothing asks for

Scenario 5 requires the system to show alternative listings "based on related or similar keywords" when a search finds no exact match. Item 4 asks for search, browse, filter and compare. Similar-keyword matching is a much larger piece of work and appears in no requirement.

### 20. Who releases contact details, and when

The proposal risk table says phone numbers are shown only after an order is **confirmed**. The system context sends the seller the "buyer contact detail (post confirmation)". UC-05 success guarantee 6 says contact details are not released until the seller **accepts**, and flags that the revised form dropped the original sentence. The use case model has a "View buyer contact" use case with no requirement behind it.

"Confirmed" is ambiguous between the buyer confirming the order and the seller accepting it, and those are different points with different privacy consequences.

### 21. The CRC cards and the domain model do not line up

- The CRC User card is what the domain model calls StudentAccount.
- ListingApproval and OrderStatusChange have no CRC card, so the approval record and the status history have no owner.
- The Report card's collaborators include "Target", which is not a class in any other document.
- The Order card claims "Handover instructions", which is finding 11.
- The domain model has no Report class because reporting sits outside the vertical slice. That is a scope difference rather than an error, but both documents should say so in the same words.

### 22. The SRC is both an oversight body and an actor with system goals

`stakeholders.md` says the SRC does not use the system day to day and has not been formally consulted. `actor-and-actor-goals.md` gives it actor goals. `system-context.md` shows data flowing both ways. `usecasemodel` gives it View usage summaries and puts Resolve disputes beside it.

If the SRC has data flows it needs an interface, and item 10 only says serious disputes are escalated to it, which could be an email. Worth deciding whether the SRC is an actor at all.

### 23. The administrator is the project team or a student moderator

`actor-and-actor-goals.md` says "Project team members". `stakeholders.md` says "our team, then a student moderator". If the administrator is a team member rather than a student, the student-ID verification rule does not apply to that account, which the domain model also raises.

### 24. Acceptance criteria cover four requirements out of ten

There are scenarios for registration, login, search and the ordering path. There are none for seller accept or reject, reservation expiry, submitting a review, or reporting and disputes. The review rule in particular is the one the proposal calls out as the important business rule of the project.

### 25. The evidence log says all three items are outstanding while the Evidence folder holds five images

`problem-evidence.md` marks the WhatsApp screenshots, the interviews and the Facebook posts all as **Outstanding**. `Evidence/` contains IMG_0863, IMG_0864, IMG_0865 and two Facebook screenshots. Meanwhile the proposal section 2 presents all three as evidence collected on 7/8/2026, and stakeholders.md cites "WhatsApp group screenshots" as access evidence.

Either the log is stale and should mark items 1 and 3 as captured, or those five images are not the evidence and the log is right. As it stands the proposal claims evidence the log says was never gathered. The interview notes do appear to be genuinely missing, since there is no interview artefact in the folder.

### 26. The project is spelled four ways

TRANS-UB, TRANS UB, Trans-UB and "TRANS UB Marketplace system", plus "TRANS UB marketplace hub" in the UC-05 scope field and "TRANS UB SYSTEM" on the use case diagram.

---

## Diagram and repository housekeeping

### 27. Use case model notation

- One relationship is labelled **"exchange"**, which is not a UML use case relationship. UML has include, extend and generalisation.
- The include stereotype is spelled "include" four times and "includes" once on the same diagram, and extend is spelled "extends".
- "Perfomance" is misspelled in "Generate Perfomance Metrics".
- In the `.drawio` source, 17 of the 28 association lines have no source or target attached to a shape. They are floating lines positioned by coordinates. They look connected now, but if anyone moves an actor or a bubble the lines will not follow. Worth opening in draw.io and reattaching the endpoints before this goes in a report.

### 28. Every text file in the repository has had its line endings rewritten

`git status` shows 22 files modified. `git diff --stat` counts 1090 changed lines. With whitespace ignored it counts 11, and all of those are real edits to the domain model files. So 20 files show as fully rewritten while containing no change at all.

If this is committed, every one of those files looks rewritten in the history, review becomes useless, and anyone else on the team who has edited the same files hits a conflict on every line. A `.gitattributes` with `* text=auto` is the usual fix, and it is better done before the next commit than after.

### 29. Placeholder files

`Prototype/prototype` is 4 bytes and `Tests/tests` is 2 bytes. Fine as directory placeholders, but worth replacing with a README or a `.gitkeep` so they do not read as empty deliverables.

---

## If the team only has time for five

1. Settle the cart. It moves FR-05, UC-05, the domain model, the glossary and four acceptance scenarios.
2. Settle when a listing becomes Reserved, because business-rules currently contradicts the requirement the vertical slice rests on.
3. Renumber the requirements so an FR id means one thing, and split item 1 while doing it.
4. Agree one list of order states, put it in the glossary, and make every other document use those words.
5. Pick one set of use case names and use it in the use case model, the traceability matrix and UC-05.

Findings 7, 8 and 11 come next, since two of them put the use case model against three other documents and the third contradicts a ratified decision.
