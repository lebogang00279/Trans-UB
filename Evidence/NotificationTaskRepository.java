public interface NotificationTaskRepository {
    NotificationTask claimNextPendingTask();
    void updateTaskStatus(NotificationTask task);
} 
