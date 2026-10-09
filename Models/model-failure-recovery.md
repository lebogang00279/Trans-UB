# DEP-01 Notification Failure and Recovery Interaction Model

```mermaid
sequenceDiagram
    autonumber
    actor Buyer
    participant Request as Request Process (web-1)
    participant DB as Transactional Store (DB)
    participant Worker as Background Process (worker-1)
    participant Provider as Notification Provider

    Buyer->>Request: 1. Reserve Listing
    Request->>DB: 2. Atomic Commit (Order + Status + Notification)
    DB-->>Request: 3. Commit Success
    Request-->>Buyer: 4. Order Reserved (201)

    Note over Worker, DB: Asynchronous Notification Processing
    Worker->>DB: 5. Poll Pending Notifications
    Worker->>DB: 6. Claim Job (Mark Processing)
    Worker->>Provider: 7. POST Notification (HTTPS)
    
    Note over Provider: Timeout / 50x Error
    Provider--xWorker: Connection Timeout

    Worker->>DB: 8. Update DeliveryOutcome (FAILED, attempts++)
    
    Note over Worker, DB: Background Retry Loop
    Worker->>DB: 9. Poll Retryable Jobs
    Worker->>Provider: 10. Retry Notification (HTTPS)
    Provider-->>Worker: 11. 200 OK Success
    Worker->>DB: 12. Update DeliveryOutcome (DELIVERED)