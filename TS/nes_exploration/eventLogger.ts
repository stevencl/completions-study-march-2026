export class EventLogger {
  log: string[] = [];

  logEvent(source: string, message: string): void {
    /** Log an event from a given source. */
    const entry = `[${source}] ${message}`;
    this.log.push(entry);
  }

  getRecent(count: number = 5): string[] {
    /** Return the most recent log entries. */
    return this.log.slice(-count);
  }
}
