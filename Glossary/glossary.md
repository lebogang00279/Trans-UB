# TRANS-UB — Glossary

Terms as used across the project documents ([Docs/project-proposal-and-approval.md](../Docs/project-proposal-and-approval.md), [Decisions/D-001.md](../Decisions/D-001.md), [Models/system-context.md](../Models/system-context.md)).

| Term | Definition |
|---|---|
| **TRANS-UB** | Working title of the project: a central online marketplace for University of Botswana students to list, find, compare and order goods and services from other students. |
| **Student Buyer** | A verified UB student using the platform to search, compare and order listings, and to confirm receipt and leave reviews. |
| **Student Seller** | A verified UB student who creates and manages listings, fulfils orders, and arranges handover with buyers. |
| **Listing** | A single item or service posted for sale by a Student Seller, with a category, price and availability status. |
| **Listing status** | The lifecycle state of a listing: **Available** (can be ordered), **Reserved** (an order against it is pending handoff), **Sold**/**Unavailable** (no longer orderable). |
| **Order** | The record created when a buyer confirms a cart, tracking the transaction between a specific buyer and seller for a specific listing. |
| **Order status** | The lifecycle state of an order: **Pending handoff** → **Delivered** (seller-marked) → **Completed** (buyer-confirmed), or **Cancelled**. |
| **Handoff / handover** | The offline, in-person exchange of the item or service and payment between buyer and seller, arranged outside the platform (see [Decisions/D-001.md](../Decisions/D-001.md)). |
| **Verification (student ID verification)** | The registration check tying an account to a valid UB student ID; simulated with synthetic data in the prototype rather than connected to real university systems. |
| **Review** | A rating and comment a buyer may submit about a seller. Gated so it can only be submitted once, and only after that buyer's order with that seller reaches Completed. |
| **Seller rating** | The seller's average score, recalculated only from reviews tied to Completed (confirmed) transactions. |
| **Reputation system** | The combination of order confirmation and gated reviews that lets buyers judge whether a seller is trustworthy. |
| **Platform administrator** | The role (initially the project team, later a student moderator) that approves/removes listings, suspends accounts, and resolves reports. |
| **Moderation** | The administrator's process of reviewing listings before or after they go live and acting on reports. |
| **Report** | A flag raised by a user (or the SRC) against a listing or account, routed to the Platform administrator for resolution. |
| **SRC** | Student Representative Council — the student oversight body with an interest in disputes and prohibited-goods issues; can request summaries and escalate disputes but does not use the system day to day. |
| **University Management** | Indirect stakeholder with a policy and liability interest in campus trading; has no direct access to the system (see [Models/system-context.md](../Models/system-context.md)). |
| **Vertical slice** | The single, end-to-end path (sign in → browse → order → handoff → confirm → review) the team builds first, because it produces the transaction record the rest of the system depends on. |
| **Synthetic/anonymised data** | Fabricated student accounts, listings and orders used for development and testing so no real UB student records are needed. |
