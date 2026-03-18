from notification_service import NotificationService


notifier = NotificationService()


def send_welcome(user: str):
    """Send a welcome notification to a new user."""
    notifier.send(user, f"Welcome to the platform, {user}!")
