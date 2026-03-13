class EventLogger:
    def __init__(self):
        self.log = []

    def log_event(self, source: str, message: str):
        """Log an event from a given source."""
        entry = f"[{source}] {message}"
        self.log.append(entry)

    def get_recent(self, count: int = 5) -> list:
        """Return the most recent log entries."""
        return self.log[-count:]
