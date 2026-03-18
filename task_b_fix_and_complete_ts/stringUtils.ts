export function parseConfig(text: string): Record<string, string> {
  /**
   * Parse a key=value config string into a dictionary.
   *
   * Rules:
   * - Lines starting with '#' are comments (skip them)
   * - Empty lines are skipped
   * - Keys and values are stripped of whitespace
   * - Values may contain '=' characters (e.g., URLs)
   * - Section headers like [database] group keys: "host" becomes "database.host"
   * - Keys before any section header have no prefix
   * - Duplicate keys: last value wins
   */
  const result: Record<string, string> = {};
  let currentSection: string | null = null;
  for (const rawLine of text.trim().split("\n")) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) {
      continue;
    }
    if (line.startsWith("[") && line.endsWith("]")) {
      currentSection = line.slice(1, -1);
      continue;
    }
    if (!line.includes("=")) {
      continue;
    }
    const eqIndex = line.indexOf("=");
    const key = line.slice(0, eqIndex).trim();
    const value = line.slice(eqIndex + 1).trim();
    // TODO: if inside a section, prefix the key with the section name and a dot
    result[key] = value;
  }
  return result;
}

export function truncate(text: string, maxLength: number): string {
  /**
   * Truncate text to the given maximum length.
   *
   * If the text is longer than maxLength, truncate it and append "..."
   * so the total length of the returned string is maxLength + 3.
   * If the text is already within maxLength, return it unchanged.
   *
   * @param text - The input string.
   * @param maxLength - The maximum number of characters before truncation.
   * @returns The original text if short enough, or the truncated text with "..." appended.
   */
  return ""; // TODO: implement this function
}
