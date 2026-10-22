 public class NotificationWorker {
    private final NotificationTaskRepository taskRepository;
    private final NotificationProviderPort notificationProvider;

    public NotificationWorker(NotificationTaskRepository taskRepository,
                              NotificationProviderPort notificationProvider) {
        this.taskRepository = taskRepository;
        this.notificationProvider = notificationProvider;
    }

    public void processPendingNotifications() {
        NotificationTask task = taskRepository.claimNextPendingTask();
        if (task == null) return;

        try {
            boolean success = notificationProvider.sendNotification(task);
            if (success) {
                task.markSent();
            } else {
                task.incrementRetry();
            }
        } catch (Exception e) {
            task.incrementRetry();
        } finally {
            taskRepository.updateTaskStatus(task);
        }
    }
} {
    
}
 {
    
}
