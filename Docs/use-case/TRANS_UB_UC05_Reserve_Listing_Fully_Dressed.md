# UC-05: Reserve an available listing

## Why I picked this use case

Our proposal already says the ordering path is the slice we build first, because it is the one that creates the transaction record the rest of the system leans on. The reviews rule, the seller rating and the dispute record all depend on an order existing and being in a known state, so if this use case is wrong everything downstream is wrong with it.

I kept the use case to the buyer's goal only. It starts when the buyer asks to reserve a listing and stops when the reservation exists and the seller has been told about it. What the seller then does with it, whether that is accepting, rejecting or letting it run out, is a separate goal for a separate actor, so I wrote those as related use cases instead of stretching this one across two days of real time.

The revised proposal now writes the reservation, expiry, rejection and cancellation rules out in section 6, so this use case follows that wording rather than making up its own. Where the two ever disagree, section 6 is the one to trust and this document is the one to fix.

Three of the lecturer's conditions changed this use case directly. Listings are limited to approved low-risk physical goods, so the precondition checks approval status rather than assuming any listing can be reserved. Payment and handover stay off the platform under Decision D-001, so step 3 states that plainly to the buyer instead of the system pretending to hold money. And the student-ID check is simulated with synthetic data, so the precondition says "prototype account" and does not claim anything about real UB records.

---

## Use case description

| Field | Entry |
|---|---|
| **Use case ID** | UC-05 |
| **Name** | Reserve an available listing |
| **Scope** | TRANS UB marketplace hub |
| **Level** | User goal |
| **Primary actor** | Student buyer |
| **Supporting actors** | None. The reservation deadline is kept by the hub itself, not by an outside service. |
| **Trigger** | The buyer opens an approved listing from search or browse results and asks to reserve it. |
| **Frequency** | Expected to be the most common write action in the system, since every completed transaction and every review starts here. |

### Stakeholders and interests

| Stakeholder | Interest in this use case |
|---|---|
| Student buyer | Wants the item held for them so they are not still negotiating for something another student has already taken. Wants to know how long the hold lasts and what they are committing to. |
| Student seller | Wants to be told quickly that someone wants the item, and wants the item taken off the market only while a real reservation is live. |
| Platform administrator | Wants no reservation to exist against a listing that was never approved, or that was removed after a report. |
| SRC | Wants a record of who reserved what and when, so a dispute can be traced later instead of being argued in a group chat. |

### Preconditions

1. The buyer is signed in with a prototype account whose simulated student-ID check passed at registration (FR-01).
2. The buyer's account is active and not suspended following a report.
3. The listing exists, has been approved by the platform administrator (FR-03), and its status is **Available**. Every listing starts as Pending Approval and is not visible to buyers until that approval happens, so an unapproved listing can never be reached from search in the first place.
4. The listing is for a low-risk physical good. Food, medicines, alcohol, stolen or suspected stolen property, restricted or dangerous products and high-risk services cannot reach an approved state at all, so they never satisfy precondition 3.
5. The buyer is not the seller of the listing.

### Success guarantee (postconditions on success)

1. An order exists with status **Pending**, linked to exactly one buyer, one seller and one listing.
2. The listing status is **Reserved**, and no other buyer can reserve it while that order is Pending.
3. A response deadline 24 hours from creation is recorded against the order (FR-07).
4. The seller can see the pending order and the buyer can see the order reference, its status and its deadline.
5. The status change is written to the order's history with the actor who caused it and the time it happened.
6. Contact details have **not** been released to either party yet. That only happens once the seller accepts, and handover is then arranged for a public, visible place on campus. *(The first proposal said phone numbers appear only after an order is confirmed. The revised form dropped that sentence, so the team needs to confirm it still holds. See open issues.)*

### Minimal guarantee (postconditions on failure)

No order record is created, the listing keeps the status it already had, no contact details are released, and the buyer is told in plain terms why the reservation did not go through. The system never leaves a listing marked Reserved without a matching order behind it.

---

## Main success scenario

1. The buyer opens an approved listing and asks to reserve it.
2. The hub confirms the listing is still Available and that the buyer is eligible to reserve it.
3. The hub tells the buyer what reserving means: the item is held for them, the seller has 24 hours to accept or reject, the buyer can cancel any time before the seller records the handover, and payment and collection are arranged directly between the two students. It states that the hub does not process or verify payment and is not an official University payment or delivery service, and it recommends meeting at a public, visible place on campus.
4. The buyer confirms and may add a short note, such as a preferred handover time.
5. The hub creates the order as Pending, moves the listing to Reserved, and records the 24-hour deadline.
6. The hub tells the seller a pending order is waiting, and shows the buyer the order reference, the current status and the deadline.

---

## Alternative flows (extensions)

**2a. The listing is no longer Available.**
It was reserved by another buyer, marked sold or unavailable by the seller, rejected by the administrator, or removed, between the buyer opening the page and confirming.
2a1. The hub refuses the reservation and creates no order.
2a2. The hub explains why, refreshes the listing state the buyer is looking at, and offers approved listings in the same category.
*(This is the failure case named in section 7 of the revised proposal.)*

**2b. The listing was removed or suspended by the administrator after the buyer opened it.**
2b1. The hub refuses the reservation.
2b2. The hub tells the buyer the listing is no longer available, without repeating the moderation reason or naming who reported it.

**2f. The seller edited the listing in an important way and it returned to Pending Approval.**
Under the listing-approval rule in section 6, a significant change sends a listing back for approval, which takes it out of the buyer's reach mid-session.
2f1. The hub refuses the reservation and creates no order.
2f2. The hub tells the buyer the listing is being checked again and may reappear. We have not agreed which edits count as important, which is a rule the team owes the class diagram.

**2c. The buyer is the seller of the listing.**
2c1. The hub refuses and explains that a seller cannot reserve their own item. This keeps a seller from manufacturing a completed order and reviewing themselves.

**2d. The buyer's account is suspended.**
2d1. The hub refuses and points the buyer to the way of contacting the administrator about the suspension. It does not reveal which report caused it.

**2e. The buyer already has a Pending order on this same listing.**
2e1. The hub does not create a second order. It returns the existing one with its reference and deadline. A double tap on a slow connection must not produce two reservations.

**5a. Two buyers confirm at nearly the same moment.**
5a1. Exactly one reservation succeeds. The listing moves to Reserved once.
5a2. The other buyer is handled as in 2a.

**5b. The hub cannot store the order.**
5b1. No order is created and the listing stays Available.
5b2. The buyer is told the reservation did not go through and can try again. A half-written reservation is worse than no reservation, because the seller would lose the item from the market with nobody holding it.

**6a. The seller cannot be notified straight away.**
6a1. The order still stands. The reservation is not rolled back because a message failed.
6a2. The hub retries the notification, and the order is waiting on the seller's dashboard when they next sign in.

---

## What happens after this use case ends

These are separate use cases, but they are the only ways the state this one creates can be resolved:

| Event | Resulting order status | Listing returns to | Requirement |
|---|---|---|---|
| Seller accepts | Accepted | stays Reserved | FR-06 |
| Seller rejects, buyer informed | Rejected | Available | FR-06 |
| Seller does not respond within 24 hours | Expired | Available | FR-07 |
| Buyer cancels before the seller records the handover | Cancelled | Available | FR-07 |
| Seller records handover | Delivered | stays Reserved | FR-08 |
| Buyer confirms receipt | Completed | Sold | FR-08 |
| Either party reports the listing, user or order | order stays as it is, report saved for the administrator | unchanged | FR-10 |

Only a Completed order unlocks a review, and only one review per order (FR-09).

Two names in this table are mine rather than the proposal's. Section 8 of the revised form lists the states as Pending Approval, Available, Reserved, Rejected, Expired, Cancelled, Delivered and Completed, which leaves no name for an order the seller has accepted but not yet handed over, and no name for a listing after completion. I used **Accepted** and **Sold** so the lifecycle has no gaps, and flagged both below so the team can either adopt them or correct me.

---

## Quality requirements attached to this scenario

1. **Visibility.** After the buyer confirms, the listing must stop appearing as available to other buyers, and the seller must be able to see the pending order, within 30 seconds. I took the 30-second figure from the Session 05 example rather than from any measurement of our own, so it is a target we still have to test.
2. **No double reservation.** Under two simultaneous confirmations, exactly one order is created. This is the check I most want in our test plan, because it is the one a demo will not catch by accident.
3. **Slow connection.** The whole reservation is one page submission and one response, so it works on campus mobile data without waiting on background requests.
4. **Auditability.** Every status change stores the actor and the time, so the administrator and the SRC can reconstruct what happened when a dispute is escalated.

---

## Traceability

| Requirement | Where it appears here |
|---|---|
| FR-01 registration and login | Precondition 1 |
| FR-03 listing approvals | Precondition 3, extension 2b |
| FR-04 search and browse | Trigger |
| FR-05 reserve or order an item | Main success scenario, extensions 2a and 5a |
| FR-06 accept or reject orders | Post-use-case table |
| FR-07 expiry and cancellation | Success guarantee 3, post-use-case table |
| FR-10 reporting and disputes | Precondition 2, extension 2d, quality requirement 4 |
| Decision D-001, payments and handover off platform | Main step 3, success guarantee 6 |
| Objective 4, clear rules so each transaction has a clear status | Success guarantee 1 to 3, follow-on table |
| Section 6 rule, listing approval | Precondition 3, extensions 2b and 2f |
| Section 6 rule, reservation | Success guarantee 2, extension 5a |
| Section 6 rule, reservation expiry and no-response | Success guarantee 3 |
| Section 6 rule, offline payment and handover, public meeting place | Main step 3 |
| Section 7 failure to test, ordering an unavailable listing | Extension 2a, minimal guarantee |

---

## Open issues

- We have not decided whether a buyer can hold several pending reservations at once, or how many. Until we do, extension 2e only covers the same-listing case.
- We have not decided whether the 24-hour clock keeps running overnight and over weekends, or only during campus hours.
- We have not decided whether an expired order counts against the seller's rating. It is not a review, so under FR-09 it currently does not, but the team should agree that deliberately.
- The revised workflow in section 7 has the buyer confirming an order straight from the listing, but the failure test in the same section still mentions refreshing the cart state. We need to say plainly whether there is a cart in the first build. I wrote this use case without one, since the workflow does not use one.
- Section 8 of the revised form does not name a state for an accepted order or for a listing after completion. I used Accepted and Sold; the team should either add them to the proposal or tell me the intended names.
- The revised form no longer says phone numbers are shared only after an order is confirmed. Success guarantee 6 still assumes it, because releasing contact details before the seller has accepted would undo the point of moderation.
- Section 6 says a listing changed "in an important way" returns to Pending Approval, but does not say which changes count. Extension 2f depends on that answer.
