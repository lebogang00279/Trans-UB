# CSI473 — Software Design and Architecture

## Project Problem Proposal and Approval Form

*Completed for Laboratory 2 and the Moodle approval checkpoint*

| Field | Team response |
|---|---|
| Team number | No.9 |
| Working project title | TRANS UB — University of Botswana Student Marketplace Hub |
| Members and student IDs | Letlhabile Xoliso Serufo — 202302072<br>Lebogang Rantlheng — 202400279<br>Tshegofatso Botho Wakwena — 202302811<br>Amanda Mapete — 202303699<br>Lame Vambu — 202203427 |
| Repository URL | https://github.com/lebogang00279/Trans-UB |
| Proposal tag/commit | Project problem proposal |
| Date submitted | 10 August 2026 |

---

## 1. Problem statement

At the University of Botswana a large number of students already sell to each other. They sell food, clothes, hair products, phone accessories, second-hand textbooks and small services such as printing, braiding and nail work. All of this trading happens informally, mostly through WhatsApp groups, Facebook posts, notice boards and word of mouth. There is no single place a student can go to see what is on sale on campus at a given time. Because of this, sellers only reach the few groups they happen to belong to, and buyers often cannot find a product at the moment they actually need it. Nothing about past dealings is recorded, so a new seller has no way of showing that they are reliable and a buyer has no way of checking whether a seller has delivered before. We are aware of students who paid first and never received the item, and their only option was to complain in the same group chat. Prices are also spread across many separate posts, so comparing two sellers means scrolling through days of messages. The people affected are student business owners, who lose sales they could have made; student customers, who carry the risk every time they buy; and indirectly the SRC and university management, who deal with the disputes and the reputational side of uncontrolled trading on campus. Without a central and more trustworthy place to trade, this campus market stays inefficient and students keep losing money they should not lose.

---

## 2. Evidence of the problem

| Evidence/source | Date/origin | What it shows |
|---|---|---|
| Screenshots of an active UB student "buy and sell" WhatsApp group | Collected 7/8/2026, group is student-run | Selling is happening at scale but with no structure: no seller profiles, no verification and listings that disappear as the chat moves on. |
| Short interviews with five student sellers and five student buyers | Conducted 7/8/2026, UB main campus | Sellers said their main problem is being seen and being believed by new customers. Buyers said they have either been let down after paying or cannot tell who is safe to buy from. |
| Facebook posts advertising items to UB students | Sampled 7/8/2026, public group | The same item is advertised at different prices in different posts, and there is no way for a buyer to compare offers side by side. |

See [Evidence/problem-evidence.md](../Evidence/problem-evidence.md) for the evidence log and outstanding artefact capture.

---

## 3. Goal and objectives

| Item | Team response |
|---|---|
| Goal | To design and build a central online marketplace for University of Botswana students, where verified student sellers can list goods and services and student buyers can search, compare and order in one place, with a reputation record that makes it easier to tell trustworthy sellers apart. |
| Objective 1 | Provide one searchable catalogue of student listings, organised by category, so a buyer can find what is available on campus without joining several group chats. |
| Objective 2 | Let buyers compare listings on price, category and seller rating before committing to an order. |
| Objective 3 | Build trust by verifying accounts against a student ID at registration and allowing a seller to be reviewed only by a buyer whose transaction with that seller has been confirmed. |

---

## 4. Stakeholders

See [Docs/stakeholders.md](stakeholders.md) for the full stakeholder table.

---

## 5. Scope, assumptions and constraints

See [Docs/problem-and-scope.md](problem-and-scope.md) for the full scope, assumptions and constraints tables.

---

## 6. Proposed core workflow / vertical slice

Primary actor: a student buyer. The slice below is the one we intend to build end to end first, because it is the path that creates the transaction record everything else depends on.

1. The buyer signs in with an account that was verified against a student ID at registration.
2. The buyer searches or filters the catalogue by category and price and opens a listing to compare it with similar ones, including the seller's rating.
3. The buyer adds the item to the cart and confirms the order. The system creates an order record with the status Pending handoff and marks that listing as reserved so it is not sold twice.
4. The seller sees the new order on their dashboard, contacts the buyer and arranges the handoff on campus, then marks the order as delivered.
5. The buyer confirms that they received the item, which moves the order to the status Completed. This confirmation is the state the rest of the system depends on.
6. Rule to enforce: only a buyer with a Completed order against that seller may submit a review, and only one review per order. The seller's average rating is then recalculated from confirmed transactions only.
7. State/result created: a stored order with its status history, a listing whose availability has changed, and a review that is permanently linked to a real transaction.
8. Failure/exception to test: the buyer tries to confirm an order for a listing the seller has already marked sold or unavailable. The system must reject the confirmation, leave no order record behind, tell the buyer clearly why it failed, and update the cart.

This offline handoff/payment approach is a settled design decision — see [Decisions/D-001.md](../Decisions/D-001.md).

---

## 7. Design-suitability check

| Check | Yes/No | Short evidence |
|---|---|---|
| Clear stakeholders and a genuine current problem | Yes | Student sellers and buyers were interviewed, and the informal trading in WhatsApp and Facebook groups is visible today. |
| At least one state-sensitive workflow or entity | Yes | An order moves through Pending handoff, Delivered, Completed or Cancelled, and a listing moves between Available, Reserved and Sold. |
| Important business/validation/security rule | Yes | A review can only be written by a buyer with a confirmed, completed transaction with that seller, and accounts must pass student ID verification. |
| Relevant quality trade-offs | Yes | Stricter verification improves trust but slows down registration; moderating listings before they appear improves safety but delays sellers. |
| Relevant failure/exception condition | Yes | Ordering an item that has already been sold, tested as described in section 6. |
| Feasible semester-sized vertical slice | Yes | The slice is list, browse, order, confirm and review. Payment, delivery and fraud detection are all out of scope. |
| Synthetic/anonymised data is sufficient | Yes | We will create fake student accounts, listings and orders for testing. No real student records are needed. |
| Not the University Service Hub or a renamed copy | Yes | This is a student-to-student marketplace with a seller reputation system, not a service request hub. |

---

## 8. Data, ethics, safety and dependency risks

| Risk/concern | How the team will control it |
|---|---|
| Fake or unauthorised users signing up as students | Require student ID verification at registration and let an administrator suspend an account. Verification is simulated with synthetic data for the prototype. |
| Sellers listing harmful, stolen or prohibited goods | Keep a banned item list, require administrator approval before a listing goes live, and give every user a way to report a listing. |
| Collecting more personal data than we need | Only store what the transaction needs: name, student number, contact detail and listing information. Phone numbers are shown only after an order is confirmed. |
| Scammers posing as sellers or buyers | Tie reviews to confirmed transactions so ratings cannot be faked, keep a record of order history, and allow reporting and suspension. |
| Personal information leaking through the prototype | Use synthetic data during development and testing, hash passwords, and keep the database off public access. |
| Dependency on free hosting and tools | Keep the code in the team repository so it can be redeployed elsewhere, and avoid features that depend on a paid service. |
| Team-level risk of losing work or falling behind | Use the shared repository with regular commits, split the work by module, and keep a weekly checklist against the semester plan. |

---

## 9. Lecturer decision

| Decision | Select one |
|---|---|
| Approved | [ ] |
| Approved with minor conditions | [ ] |
| Revise and resubmit | [ ] |

| Field | Complete |
|---|---|
| Conditions/comments | |
| Lecturer | Dr Cleverence Kombe |
| Decision date / resubmission date if applicable | |
