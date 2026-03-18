import { summarizeScores } from "./studentSummary";

describe("summarizeScores", () => {
  test("two subjects", () => {
    const records = [
      { name: "Alice", subject: "Math", score: 90 },
      { name: "Bob", subject: "Math", score: 80 },
      { name: "Alice", subject: "English", score: 85 },
      { name: "Bob", subject: "English", score: 95 },
    ];
    const result = summarizeScores(records);
    expect(result["Math"]["average"]).toBe(85.0);
    expect(result["Math"]["top_scorer"]).toBe("Alice");
    expect(result["English"]["average"]).toBe(90.0);
    expect(result["English"]["top_scorer"]).toBe("Bob");
  });

  test("single record", () => {
    const records = [{ name: "Charlie", subject: "Science", score: 72 }];
    const result = summarizeScores(records);
    expect(result["Science"]["average"]).toBe(72.0);
    expect(result["Science"]["top_scorer"]).toBe("Charlie");
  });

  test("three students one subject", () => {
    const records = [
      { name: "Alice", subject: "Math", score: 70 },
      { name: "Bob", subject: "Math", score: 90 },
      { name: "Charlie", subject: "Math", score: 80 },
    ];
    const result = summarizeScores(records);
    expect(result["Math"]["average"]).toBe(80.0);
    expect(result["Math"]["top_scorer"]).toBe("Bob");
  });

  test("tied scores returns first", () => {
    const records = [
      { name: "Alice", subject: "Art", score: 95 },
      { name: "Bob", subject: "Art", score: 95 },
    ];
    const result = summarizeScores(records);
    expect(result["Art"]["average"]).toBe(95.0);
    expect(result["Art"]["top_scorer"]).toBe("Alice");
  });
});
