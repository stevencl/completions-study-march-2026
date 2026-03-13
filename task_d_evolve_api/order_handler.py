from notification_service import NotificationService


notifier = NotificationService()


def place_order(user: str, item: str):
    """Process a new order and notify the user."""
    print(f"Processing order for {item}...")
    notifier.send(user, f"Your order for {item} has been placed.")


def cancel_order(user: str, order_id: str):
    """Cancel an existing order and notify the user."""
    print(f"Cancelling order {order_id}...")
    notifier.send(user, f"Your order {order_id} has been cancelled.")
