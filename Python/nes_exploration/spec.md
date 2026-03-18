# NES Exploration Task

This is a short guided task to explore Next Edit Suggestions (NES).

## Your task

1. In `event_logger.py`, add an `urgent: bool = False` parameter to the `log_event()` method.

2. Update the formatted entry so that urgent events are prefixed with `[URGENT]`:
   - Normal: `[auth] user logged in`
   - Urgent: `[URGENT][system] Error 500: database timeout`

3. In `handlers.py`, update the `handle_error()` call to pass `urgent=True`.
   Leave the other two calls unchanged.

**As you make these changes, pay attention to any suggestions the editor offers about where to edit next.**
