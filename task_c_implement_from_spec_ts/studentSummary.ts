interface StudentRecord {
  name: string;
  subject: string;
  score: number;
}

interface SubjectSummary {
  average: number;
  top_scorer: string;
}

export function summarizeScores(
  records: StudentRecord[]
): Record<string, SubjectSummary> {
  /**
   * Summarize student scores by subject.
   *
   * @param records - A list of objects, each with 'name', 'subject', and 'score' keys.
   * @returns An object mapping each subject to { average: number, top_scorer: string }.
   */
  return {}; // Your implementation here
}
