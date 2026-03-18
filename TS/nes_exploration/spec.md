# NES Exploration Task

This is a short guided task to explore Next Edit Suggestions (NES).

## Your task

1. In `eventLogger.ts`, add an `urgent: boolean = false` parameter to the `logEvent()` method.

2. Update the formatted entry so that urgent events are prefixed with `[URGENT]`:
   - Normal: `[auth] user logged in`
   - Urgent: `[URGENT][system] Error 500: database timeout`

3. In `handlers.ts`, update the `handleError()` call to pass `true` for the `urgent` parameter.
   Leave the other two calls unchanged.

**As you make these changes, pay attention to any suggestions the editor offers about where to edit next.**
