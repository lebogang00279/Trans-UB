TRANS-UB Lab 07 Evidence

Purpose

This folder records the repository evidence produced for CSI473 Lab 07. The lab focuses on translating selected quality scenarios into architectural obligations, comparing realistic architecture alternatives, defining the component/module architecture, recording the architectural decision, and identifying the highest architectural risk.

Lab 07 Evidence Files

The following artefacts are part of the Lab 07 evidence:

• docs/architecture-options.md
Compares the main architecture alternatives considered for TRANS-UB using the same criteria.
• docs/quality-to-architecture.md
Maps selected quality scenarios to concrete architectural obligations, module responsibilities, interfaces, transaction rules and failure boundaries.
• models/component-architecture.mmd
Editable Mermaid source for the TRANS-UB component/module architecture.
• models/component-architecture.svg
Readable SVG export of the component/module architecture.
• decisions/ADR-001-architecture.md
Records the architecture decision, its context, alternatives, rationale, and positive/negative consequences.

Selected Architecture

TRANS-UB uses a modular layered monolith.

The main modules are:

• Account / Authentication
• Listing Management
• Order / Reservation Management
• Review Management
• Reporting / Moderation
• Notification
• Persistence / Database Access

This architecture keeps deployment simple while providing clearer responsibility boundaries and lower coupling than a basic layered monolith.

Main Architecture Drivers

The architecture is influenced by the following concerns:

1. Prevent duplicate live reservations for the same listing.
2. Keep Listing and Order states consistent.
3. Re-check listing availability immediately before reservation confirmation.
4. Ensure notification failure does not roll back a successful reservation.
5. Enforce buyer, seller and Platform Administrator permissions.
6. Allow reviews only after completed transactions.
7. Keep payment and physical handover outside TRANS-UB.
8. Keep the prototype simple enough to implement and test within the project schedule.

Highest Architectural Risk

The highest architectural risk is inconsistent Listing and Order state during simultaneous reservation attempts.

If two buyers try to reserve the same Available listing at nearly the same time, the architecture must guarantee that only one request succeeds.

The architectural response is to:

• re-check availability immediately before reservation;
• create the Pending Order;
• record the OrderStatusChange;
• change the Listing from Available to Reserved;
• commit the required changes atomically;
• reject the competing request if the listing is no longer Available.

Notification delivery is outside the core reservation transaction. A notification failure must be recorded but must not undo a valid reservation.

Repository Evidence

Lab 07 evidence should be committed to the shared repository before leaving the laboratory.

Screenshots alone are not source evidence. Editable source files and readable exports should both be retained.

Expected repository structure:

docs/

├── architecture-options.md

└── quality-to-architecture.md

models/

├── component-architecture.mmd

└── component-architecture.svg

decisions/

└── ADR-001-architecture.md

evidence/

└── lab-07/

    └── README.md

Revision Record

Final Lab 07 artefacts should be committed after the architecture review and revision.

• Commit message: Finalize Lab 07 architecture evidence
• Commit hash: [add final commit hash after committing]
• Highest architectural risk recorded: Yes
• Editable component source included: Yes
• Readable component export included: Yes
