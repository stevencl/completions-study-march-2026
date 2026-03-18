import { NotificationService } from "./notificationService";

const notifier = new NotificationService();

export function placeOrder(user: string, item: string): void {
  /** Process a new order and notify the user. */
  console.log(`Processing order for ${item}...`);
  notifier.send(user, `Your order for ${item} has been placed.`);
}

export function cancelOrder(user: string, orderId: string): void {
  /** Cancel an existing order and notify the user. */
  console.log(`Cancelling order ${orderId}...`);
  notifier.send(user, `Your order ${orderId} has been cancelled.`);
}
