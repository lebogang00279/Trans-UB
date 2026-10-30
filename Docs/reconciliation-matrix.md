# TRANS-UB Phase 2 — Reconciliation Matrix

| Requirement / scenario | Implementation | Test evidence | Actual result |
|---|---|---|---|
| FR-05 / UC-05 successful reservation | `src/transub/service.py` | `test_success` | PASS |
| Invalid request | `src/transub/service.py` | `test_invalid` | PASS |
| Own-listing rule | `src/transub/service.py` | `test_own_listing` | PASS |
| Ineligible buyer | `src/transub/service.py` | `test_ineligible` | PASS |
| Duplicate reservation prevention | `schema/schema.sql`, `src/transub/service.py` | `test_duplicate` | PASS |
| Simultaneous reservation integrity | SQLite `BEGIN IMMEDIATE` + unique live-order index | `test_concurrent_exactly_one` | PASS |
| Notification failure tolerance | `FailingNotification`, notification outside core transaction | `test_notification_failure` | PASS |
| HTTP vertical slice | `src/transub/api.py` | Manual smoke test with POST request | PASS |

## Smoke-test result
A real POST to `/api/listings/LIST-104/reserve` returned a Pending Order with the Listing in Reserved state and notification outcome DELIVERED.

## Scope limitation
This runnable Phase 2 slice implements UC-05 only. Other marketplace functions remain design-level evidence unless separately implemented.
