public class ReserveListingUseCase {
    private final OrderRepository orderRepository;

    // Dependency Injection: High-level module depends on abstractions
    public ReserveListingUseCase(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    public Order execute(String buyerId) {
        Order order = new Order(buyerId);
        order.reserve();

        NotificationTask task = new NotificationTask(order.getOrderId());

        // Atomic commit to transactional database
        orderRepository.saveAtomicOrderAndNotification(order, task);
        return order;
    }
} {
    
}
