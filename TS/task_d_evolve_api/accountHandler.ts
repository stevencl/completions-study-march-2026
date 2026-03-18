import { NotificationService } from "./notificationService";

const notifier = new NotificationService();

export function sendWelcome(user: string): void {
  /** Send a welcome notification to a new user. */
  notifier.send(user, `Welcome to the platform, ${user}!`);
}
