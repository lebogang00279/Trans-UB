# TRANS-UB Lab 10 — UI Alternative States

| State | Trigger | UI response |
|---|---|---|
| Loading | Data is being fetched | Show progress and retain page/task context. |
| Empty | No listings match | Show “No matching listings” and clear/change filters action. |
| Validation | Input invalid | Preserve input; identify field and correction in text. |
| Unauthenticated | Reserve without session | Explain sign-in requirement; preserve intended listing where possible. |
| Unauthorised | Wrong role attempts protected action | Show clear permission message. |
| Unavailable / stale | Final availability recheck fails | Show current status, create no Order, return to refreshed results. |
| Duplicate request | Reservation submitted twice | Do not create second live Order; show existing/current result. |
| Server error | Atomic reservation fails | State that reservation was not completed; allow safe retry. |
| Notification failure | Reservation succeeds but seller notification fails | Show reservation success; notification failure must not reverse it. |
| Offline / disconnected | Client loses network before outcome known | Tell user outcome is unknown and to check My Orders before retrying. |

All statuses must use text/non-colour cues. Colour alone must not communicate state.
