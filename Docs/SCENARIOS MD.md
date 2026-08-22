1\. Search Performance

Source / Stimulus: A student searches for a textbook or other item.

Environment: Student Hub is operating normally.

Artifact: Student Hub search and listing service.

Response: The system retrieves and displays the relevant listings.

Measure: Search results should be visible within 2 seconds for at least 95% of searches.

2\. Listing Performance

Source / Stimulus: A student selects a product listing to view its details.

Environment: Student Hub is operating normally.

Artifact: Product listing and listing-details service.

Response: The system displays the current product information, price, seller details, and availability.

Measure: The listing details should be displayed within 2 seconds for at least 95% of requests.

3\. Student Verification / Access Control

Source / Stimulus: An unverified student attempts to create a listing.

Environment: The student has registered but has not completed student verification.

Artifact: Student Hub seller and listing functions.

Response: The system rejects the request and prevents the student from publishing the listing.

Measure: 100% of listing attempts by unverified students must be rejected.

4\. Listing Validation

Source / Stimulus: A seller submits a listing with required information missing.

Environment: The seller is creating a new listing.

Artifact: Listing record and validation service.

Response: The system rejects the incomplete listing and identifies the information that is missing.

Measure: 100% of incomplete listings must be rejected before publication.

5\. Order Reliability

Source / Stimulus: A buyer confirms an order.

Environment: Student Hub is operating normally.

Artifact: Order record and listing status.

Response: The system records the order and correctly updates the relevant order/listing status.

Measure: 99% of valid order confirmations should be completed within 3 seconds without data loss.

6\. Duplicate Order Prevention

Source / Stimulus: A buyer submits the same order more than once.

Environment: Student Hub is processing the order.

Artifact: Order record and order-confirmation process.

Response: The system recognises the repeated submission and keeps only one valid order.

Measure: Zero duplicate orders should be created from repeated identical submissions.

7\. Messaging Service Failure

Source / Stimulus: A buyer sends a message to a seller while the messaging service is unavailable.

Environment: The external messaging service is temporarily unavailable.

Artifact: Student Hub communication request.

Response: The system preserves the message for retry or clearly informs the user that delivery has failed rather than silently losing the message.

Measure: 100% of submitted messages must either be delivered or retained for retry.

8\. Listing Update Integrity

Source / Stimulus: A seller changes information on an existing listing.

Environment: The listing already exists in Student Hub.

Artifact: Listing record.

Response: The system updates the intended listing without changing another seller's listing.

Measure: 100% of valid listing updates must be applied to the correct listing only.

9\. Review Integrity

Source / Stimulus: A buyer attempts to submit a review for a transaction that has not been confirmed.

Environment: The transaction is still unconfirmed.

Artifact: Review and transaction records.

Response: The system rejects the review because the transaction has not been confirmed.

Measure: 100% of reviews linked to unconfirmed transactions must be rejected.

10\. Stale Listing / Order Conflict

Source / Stimulus: A buyer attempts to order an item using listing information that is no longer current.

Environment: The seller has changed the listing's availability or status since the buyer viewed it.

Artifact: Listing and order records.

Response: The system detects the outdated information and prevents an invalid order, or requires the buyer to use the current listing information.

Measure: 100% of orders based on outdated or unavailable listing states must be rejected or reconciled before confirmation.