# Task D: Evolve an API

You have a small working codebase with three files:
- `notification_service.py` — A `NotificationService` class with a `send(user, message)` method
- `order_handler.py` — Two functions that call `notifier.send()` to notify users about orders
- `account_handler.py` — One function that calls `notifier.send()` to welcome new users

**Running the tests:** Open a terminal in this folder and run:
```
python -m pytest test_notification_service.py -v
```
All 5 tests should pass when you're done.

**Your task:** Make the following three changes:

---

## 1. Add a `priority` parameter to `send()`

In `notification_service.py`, add a `priority` parameter to the `send()` method with a default value of `"normal"`.

Update the notification format to include priority:
```
[NORMAL] To alice: Your order has been placed.
[HIGH] To alice: Your order has been cancelled.
```

The priority label should be uppercase in the formatted string.

---

## 2. Update order notifications to use high priority

In `order_handler.py`, update **both** calls to `notifier.send()` to pass `priority="high"`.

The `send_welcome()` call in `account_handler.py` should remain at the default (normal) priority — do **not** change it.

---

## 3. Add a `format_notification()` helper method

In `notification_service.py`, add a helper method:

```python
def format_notification(self, user: str, message: str, priority: str) -> str:
```

This method should build and return the formatted notification string (e.g., `"[HIGH] To alice: message"`).

Update `send()` to use `format_notification()` internally instead of formatting the string directly.
