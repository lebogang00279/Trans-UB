
import java.time.Instant;
import java.util.UUID;

public class Order {
    private final String orderId;
    private final String buyerId;
    private OrderStatus status;

    public Order(String buyerId) {
        this.orderId = UUID.randomUUID().toString();
        this.buyerId = buyerId;
        this.status = OrderStatus.PENDING;
    }

    public void reserve() {
        this.status = OrderStatus.RESERVED;
    }

    public String getOrderId() { return orderId; }
    public String getBuyerId() { return buyerId; }
    public OrderStatus getStatus() { return status; }
}

enum OrderStatus { PENDING, RESERVED, FAILED }

class NotificationTask {
    private final String taskId;
    private final String orderId;
    private String status; // PENDING, PROCESSING, SENT, FAILED
    private int retryCount;

    public NotificationTask(String orderId) {
        this.taskId = UUID.randomUUID().toString();
        this.orderId = orderId;
        this.status = "PENDING";
        this.retryCount = 0;
    }

    public String getTaskId() { return taskId; }
    public void markProcessing() { this.status = "PROCESSING"; }
    public void markSent() { this.status = "SENT"; }
    public void incrementRetry() { this.retryCount++; }
}
