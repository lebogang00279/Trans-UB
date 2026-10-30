# TRANS-UB Phase 2 — Technical Debt and Residual Risks

## Technical debt
- Student verification is synthetic/prototype-only.
- Notification delivery uses a simple adapter rather than a production provider.
- Only the approved UC-05 reservation vertical slice is implemented end-to-end.
- The 24-hour deadline is stored, but no background scheduler automatically expires Orders.
- Production authentication, deployment hardening and monitoring are outside this academic slice.

## Residual risks
- SQLite is appropriate for the academic prototype but has not been load-tested for production use.
- Notification retry/backoff is not implemented.
- Security testing beyond the implemented business-rule checks remains future work.

## Release recommendation
**Suitable for academic Phase 2 demonstration of UC-05. Not production-ready.**
