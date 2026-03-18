import { NotificationService } from "./notificationService";

describe("NotificationService", () => {
  let service: NotificationService;

  beforeEach(() => {
    service = new NotificationService();
  });

  test("send default priority", () => {
    service.send("alice", "Hello!");
    expect(service.sentNotifications[service.sentNotifications.length - 1]).toBe(
      "[NORMAL] To alice: Hello!"
    );
  });

  test("send high priority", () => {
    service.send("bob", "Urgent!", "high");
    expect(service.sentNotifications[service.sentNotifications.length - 1]).toBe(
      "[HIGH] To bob: Urgent!"
    );
  });

  test("formatNotification normal", () => {
    const result = service.formatNotification("alice", "Test", "normal");
    expect(result).toBe("[NORMAL] To alice: Test");
  });

  test("formatNotification high", () => {
    const result = service.formatNotification("bob", "Alert", "high");
    expect(result).toBe("[HIGH] To bob: Alert");
  });

  test("history preserved", () => {
    service.send("alice", "First");
    service.send("bob", "Second", "high");
    const history = service.getHistory();
    expect(history).toHaveLength(2);
    expect(history[0]).toContain("[NORMAL]");
    expect(history[1]).toContain("[HIGH]");
  });
});
