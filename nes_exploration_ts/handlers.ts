import { EventLogger } from "./eventLogger";

const logger = new EventLogger();

export function handleLogin(username: string): void {
  /** Log a successful login event. */
  logger.logEvent("auth", `${username} logged in`);
}

export function handleError(errorCode: number, details: string): void {
  /** Log an error event. */
  logger.logEvent("system", `Error ${errorCode}: ${details}`);
}

export function handleRequest(endpoint: string, method: string): void {
  /** Log an incoming API request. */
  logger.logEvent("api", `${method} ${endpoint}`);
}
