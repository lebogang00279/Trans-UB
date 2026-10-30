# Trans-UB
CSI473 Group project
# TRANS-UB Phase 2 Runnable Vertical Slice

Implements **UC-05 — Reserve an Available Listing** using Python 3 + SQLite, standard library only.

## Setup
```bash
python3 -m src.transub.setup_db
```

## Run API
```bash
python3 -m src.transub.api
```
API: `http://127.0.0.1:8000`

## Example
```bash
curl -X POST http://127.0.0.1:8000/api/listings/LIST-104/reserve -H 'Content-Type: application/json' -d '{"buyerId":"202302072","buyerNote":"Campus collection"}'
```

## Test
```bash
python3 -m unittest discover -s tests -v
```

## Implemented evidence
- success: Pending Order + Listing Reserved + initial OrderStatusChange;
- invalid request;
- own-listing rule;
- ineligible buyer rule;
- duplicate reservation prevention;
- simultaneous reservation integrity;
- notification failure tolerance.

Student verification is synthetic/prototype-only. Payment and handover remain outside TRANS-UB.
