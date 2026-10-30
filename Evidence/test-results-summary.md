# TRANS-UB Phase 2 — Test Results Summary

## Final verification

Command:

```bash
python3 -m unittest discover -s tests -v
```

Result: **PASS**

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 718, in _warm_feature_flows
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 509, in _warm_drawing_and_image_flows
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/generated/interface/models.py", line 32861, in bring_to_front
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/rpc/remote.py", line 764, in __call__
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/rpc/client.py", line 175, in call
artifact_tool.rpc.client.RemoteError: Element ordering requires an owning element collection.
test_concurrent_exactly_one (test_reservation.T.test_concurrent_exactly_one) ... ok
test_duplicate (test_reservation.T.test_duplicate) ... ok
test_ineligible (test_reservation.T.test_ineligible) ... ok
test_invalid (test_reservation.T.test_invalid) ... ok
test_notification_failure (test_reservation.T.test_notification_failure) ... ok
test_own_listing (test_reservation.T.test_own_listing) ... ok
test_success (test_reservation.T.test_success) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.166s

OK
```

## Covered behaviours
- successful UC-05 reservation;
- invalid request handling;
- own-listing rule;
- ineligible buyer rule;
- duplicate reservation prevention;
- simultaneous reservation integrity;
- notification-failure tolerance.

These are executed results from the final clean submission package.
