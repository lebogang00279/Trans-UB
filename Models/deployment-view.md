# TRANS-UB Deployment View (DEP-01 v1)

Editable source: [Models/deployment-diagram.mmd](../Models/deployment-diagram.mmd)
Readable export: [Models/deployment-diagram.svg](../Models/deployment-diagram.svg)

This is a proposed deployment. Nothing here is installed yet, so every host below is a role the system needs rather than a machine we have been given.

## What I was trying to show

The question I worked from is the one in Session 14: what survives a restart, what does the user actually know, and who is responsible for picking the work back up. Our architecture decision in ADR-001 is a modular layered monolith, so the logical module boundaries do not change here. What changes is where those modules run and what happens when one of the runtime pieces stops.

I kept the allocation small on purpose. Seven modules does not mean seven servers.

## Nodes, artefacts and processes

| Node | Runs | Artefact | Responsibility |
|---|---|---|---|
| Student buyer device | Browser | none | Search, browse, reserve, confirm receipt, leave a review |
| Student seller device | Browser | none | Create and edit listings, accept or reject orders, mark delivered |
| Platform administrator device | Browser | none | Approve or remove listings, resolve reports, suspend accounts |
| Edge host | Reverse proxy | none | TLS termination and static files |
| Application host | web-1, worker-1 | transub-app:1.0 | Everything the application does |
| Database host | Database engine | none | The one durable store |
| Notification provider | External email or SMS service | none | Delivers the seller alert. Outside our trust boundary. |

web-1 and worker-1 run the same artefact. They are two processes, not two builds. web-1 handles anything a user triggers by clicking. worker-1 runs the things nobody clicks: retrying a notification that did not get through, and sweeping for Pending orders that have passed their 24-hour `responseDeadline` under FR-07.

I did think about putting both roles in one process. The reason I split them is that FR-07 has no user behind it. If expiry only runs inside a request, an order expires whenever the next person happens to load a page, which is not what the requirement says. The cost of splitting is that there are now two processes to watch instead of one, and a failure of the shared application host still takes out both of them. That tradeoff is on the diagram so a reviewer does not have to assume we missed it.

## Communication paths

| Path | Protocol | Notes |
|---|---|---|
| Client browsers to edge host | HTTPS | The only way in from outside |
| Edge host to web-1 | HTTP over loopback | Same host only, so it never crosses a network |
| web-1 to database | Not yet selected | Carries the reservation commit |
| worker-1 to database | Not yet selected | Claims committed pending work |
| worker-1 to notification provider | HTTPS | Sits outside the reservation transaction |

We have not picked a database yet, so I have marked both database paths as not selected rather than writing in Postgres and making it look like a decision we took. Same for the notification provider. The endpoint, the API version and the credential source are all still open, and they are the evidence the Session 14 review table asks for on a remote path.

## Durable and volatile state

Durable, in the transactional store: `StudentAccount`, `Listing`, `ListingApproval`, `Order`, `OrderStatusChange`, `Review`, `Report`, and `Notification` with its `deliveryOutcome` and `attempts`.

Volatile, lost on restart: the user's session in web-1, anything held in memory during a request, and worker-1's in-flight claim on a notification it has not finished.

The thing I want a reviewer to be able to read off the diagram is that there is no pending delivery work living only in memory. The seller notification is a row before anyone tries to send it. That is the difference between our design and the failure in the Session 14 case, where the approval committed and the delivery task did not exist anywhere outside the process that died.

Recovery owner is the Notification module running in worker-1. It owns any `Notification` row with an unresolved `deliveryOutcome`, and it owns Pending orders past their deadline.

## Failure analysis

| Interruption | Durable evidence | Truthful status | Owner and next action |
|---|---|---|---|
| web-1 restarts after the reservation commits but before the 201 reaches the buyer | Order (Pending), OrderStatusChange, Listing (Reserved), Notification row | Reservation recorded, buyer does not know yet | Order / Reservation: the buyer's order list shows the Pending order on next load. No second order is created. |
| Two buyers reserve the same listing within the same moment | One Pending Order, Listing Reserved | One succeeded, one did not | Order / Reservation: second request fails the final availability check and gets 409 `LISTING_NOT_AVAILABLE`. This is the risk already recorded in architecture-risk.md. |
| The notification provider times out | Order, Listing, Notification with the attempt recorded | Reservation stands, delivery unconfirmed | Notification in worker-1: retry. A timeout does not prove the message was not sent, so it must not be reported to the seller as failed. |
| worker-1 stops after claiming a notification | Notification row with its attempt state | Reservation stands, delivery unconfirmed | Notification in worker-1: reclaim the row after restart. Do not assume it was never sent. |
| The database host is unreachable | Whatever was committed before | No reservation can be made at all | No owner yet. See the open question below. |

## Test specifications

These are specified, not run. Nothing has been implemented, so there are no results to report.

- TEST-D1: reserve a listing, stop web-1 immediately after the commit, restart it, then load the buyer's orders. Expect exactly one Pending order and the listing in Reserved.
- TEST-D2: send two reservation requests for the same Available listing at nearly the same time. Expect one 201 and one 409, one Pending order, and no second OrderStatusChange.
- TEST-D3: make the notification provider time out, then restart worker-1. Expect the order still Pending, the listing still Reserved, and the notification attempt recorded rather than silently dropped.

## Assumptions

- Transactional storage survives a process restart. Everything above depends on this and I have not tested it.
- The edge host and the application host are inside the same trust boundary, so the loopback hop does not need TLS.
- Student identity is synthetic prototype data held in our own database. We are not calling any UB system, which is what the approved scope says.

## Open questions and one inconsistency I found

Q-D1: nothing in the design says what the user sees when the database host is unreachable. The other four rows in the failure table have an owner and a next action. This one does not, and I would rather leave it visible than write in an owner we have not agreed on.

While drawing this I noticed that `Models/component-diagram.mmd` shows `Student Identity Data` as an external store, while the SVG export of the same diagram calls it `Prototype Identity Data`. The scope table says we are not integrating with live University of Botswana student records, so the SVG is the one that matches our approved scope and the Mermaid source is wrong. The two files also differ in a few connectors. I have not touched either file because that is a separate repair, but it needs fixing before anyone reviews the component view against this one.
