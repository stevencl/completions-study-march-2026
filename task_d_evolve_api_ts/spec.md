# Task D: Evolve an API

You have a small working codebase with three files:
- `notificationService.ts` — A `NotificationService` class with a `send(user, message)` method
- `orderHandler.ts` — Two functions that call `notifier.send()` to notify users about orders
- `accountHandler.ts` — One function that calls `notifier.send()` to welcome new users

**Running the tests:** Open a terminal in this folder and run:
```
npm install
npm test
```
All 5 tests should pass when you're done.

**Your task:** Make the following three changes:

---

## 1. Add a `priority` parameter to `send()`

In `notificationService.ts`, add a `priority` parameter to the `send()` method with a default value of `"normal"`.

Update the notification format to include priority:
```
[NORMAL] To alice: Your order has been placed.
[HIGH] To alice: Your order has been cancelled.
```

The priority label should be uppercase in the formatted string.

---

## 2. Update order notifications to use high priority

In `orderHandler.ts`, update **both** calls to `notifier.send()` to pass `"high"` as the priority.

The `sendWelcome()` call in `accountHandler.ts` should remain at the default (normal) priority — do **not** change it.

---

## 3. Add a `formatNotification()` helper method

In `notificationService.ts`, add a helper method:

```typescript
formatNotification(user: string, message: string, priority: string): string
```

This method should build and return the formatted notification string (e.g., `"[HIGH] To alice: message"`).

Update `send()` to use `formatNotification()` internally instead of formatting the string directly.
