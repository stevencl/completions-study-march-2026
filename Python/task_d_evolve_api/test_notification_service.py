import unittest
from notification_service import NotificationService


class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.service = NotificationService()

    def test_send_default_priority(self):
        self.service.send("alice", "Hello!")
        self.assertEqual(self.service.sent_notifications[-1], "[NORMAL] To alice: Hello!")

    def test_send_high_priority(self):
        self.service.send("bob", "Urgent!", priority="high")
        self.assertEqual(self.service.sent_notifications[-1], "[HIGH] To bob: Urgent!")

    def test_format_notification(self):
        result = self.service.format_notification("alice", "Test", "normal")
        self.assertEqual(result, "[NORMAL] To alice: Test")

    def test_format_notification_high(self):
        result = self.service.format_notification("bob", "Alert", "high")
        self.assertEqual(result, "[HIGH] To bob: Alert")

    def test_history_preserved(self):
        self.service.send("alice", "First")
        self.service.send("bob", "Second", priority="high")
        history = self.service.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("[NORMAL]", history[0])
        self.assertIn("[HIGH]", history[1])


if __name__ == "__main__":
    unittest.main()
