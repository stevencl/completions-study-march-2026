from event_logger import EventLogger


logger = EventLogger()


def handle_login(username: str):
    """Log a successful login event."""
    logger.log_event("auth", f"{username} logged in")


def handle_error(error_code: int, details: str):
    """Log an error event."""
    logger.log_event("system", f"Error {error_code}: {details}")


def handle_request(endpoint: str, method: str):
    """Log an incoming API request."""
    logger.log_event("api", f"{method} {endpoint}")
