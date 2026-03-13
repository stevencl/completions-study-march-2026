class NotificationService:
    def __init__(self):
        self.sent_notifications = []

    def send(self, user: str, message: str):
        """Send a notification to a user."""
        notification = f"To {user}: {message}"
        self.sent_notifications.append(notification)
        print(notification)

    def get_history(self) -> list:
        """Return the list of all sent notifications."""
        return self.sent_notifications.copy()
