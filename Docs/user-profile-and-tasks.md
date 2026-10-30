# TRANS-UB Lab 10 — User Profile and Task Scenarios

## Primary user — Student Buyer
A University of Botswana student using a phone to find approved low-risk physical goods.

### Goals
- find an item quickly;
- understand price/category/status;
- reserve an Available listing in few steps;
- understand success/conflict clearly.

### Constraints / needs
- mobile-first use;
- variable network quality;
- readable labels and touch targets;
- non-colour status cues;
- clear errors;
- payment and physical handover remain outside TRANS-UB.

## Primary task — Reserve an Available Listing
**Traceability:** UC-05 / FR-05.

Shortest reasonable path:
1. Browse/search.
2. Open Available listing.
3. Tap Reserve.
4. Review terms and optional note.
5. Confirm reservation.
6. System re-checks availability.
7. Confirmation shows Order = Pending, Listing = Reserved, seller response deadline.

### Success criteria
- no shopping cart;
- Pending state is clear;
- 24-hour seller-response rule is visible;
- no payment is requested inside TRANS-UB.

## Secondary task — Administrator resolves a report
1. Open Reports.
2. Open an Open report.
3. Review target/reason/context.
4. Mark Under Review.
5. Resolve or Escalate to SRC.

Success: report state remains visible and Resolve vs Escalate are clearly different actions.
