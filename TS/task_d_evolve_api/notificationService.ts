export class NotificationService {
  sentNotifications: string[] = [];

  send(user: string, message: string): void {
    /** Send a notification to a user. */
    const notification = `To ${user}: ${message}`;
    this.sentNotifications.push(notification);
    console.log(notification);
  }

  getHistory(): string[] {
    /** Return the list of all sent notifications. */
    return [...this.sentNotifications];
  }
}
