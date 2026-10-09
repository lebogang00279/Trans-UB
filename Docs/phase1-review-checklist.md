# TRANS-UB Phase 1 Review Checklist

Complete this checklist before creating the `phase1-submission` tag.

## Scope and approval
- [ ] Low-risk physical goods only.
- [ ] Food, medicines, alcohol, stolen/restricted goods and high-risk services excluded.
- [ ] Student verification described as synthetic/prototype-only.
- [ ] Payments and physical handover outside TRANS-UB.
- [ ] Reservation expiry, rejection, cancellation, no-response, reports and disputes are defined.

## Requirements and terminology
- [ ] FR-01 to FR-10 match `Docs/requirements.md`.
- [ ] No shopping-cart workflow remains in the Phase 1 baseline.
- [ ] Order states: Pending, Accepted, Rejected, Expired, Cancelled, Delivered, Completed.
- [ ] Listing states: Pending Approval, Available, Reserved, Sold, Removed.
- [ ] Report states: Open, Under Review, Resolved, Escalated.
- [ ] Platform Administrator terminology is consistent.

## Models
- [ ] System context editable source and SVG are present/readable.
- [ ] Use-case editable source and SVG match FR-01 to FR-10.
- [ ] Domain model source/export match the glossary and responsibilities.
- [ ] Sequence source/export uses the same messages as the consistency matrix.
- [ ] Order state-machine source/export is present and readable.
- [ ] Lines and labels are readable; connectors do not run through model elements.

## Traceability and consistency
- [ ] Traceability matrix maps every FR to use case, analysis element and verification.
- [ ] Consistency matrix maps core steps to exact sequence messages, responsibilities and states.
- [ ] FR-10 maps to Report and Platform Administrator.
- [ ] No old state names such as `Pending handoff` or `Awaiting Collection`.

## Design rationale
- [ ] D-001 includes decision, rationale, alternatives and consequences.
- [ ] Architecture-driver note contains at least three project-derived drivers.
- [ ] Architecture-driver note contains at least two realistic alternatives.

## Peer review and revision
- [ ] Three highest-risk peer-review findings recorded.
- [ ] At least one high-risk issue visibly corrected.
- [ ] Revision commit made after critique.
- [ ] README links to final sources and exports.

## Submission
- [ ] Final PDF saved as `submissions/CSI473_A2_Phase1_Team9.pdf`.
- [ ] PDF opens and diagrams/tables are readable.
- [ ] `Docs/architecture-drivers.md` committed.
- [ ] `Docs/phase1-review-checklist.md` committed.
- [ ] Peer-review evidence committed.
- [ ] Final revision pushed.
- [ ] Tag `phase1-submission` created from the final revision commit and pushed.
- [ ] Moodle submission completed.