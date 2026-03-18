import { parseConfig, truncate } from "./stringUtils";

describe("parseConfig", () => {
  test("simple pairs", () => {
    const text = "name = Alice\nage = 30";
    expect(parseConfig(text)).toEqual({ name: "Alice", age: "30" });
  });

  test("comments ignored", () => {
    const text = "# This is a comment\nkey = value";
    expect(parseConfig(text)).toEqual({ key: "value" });
  });

  test("empty lines ignored", () => {
    const text = "a = 1\n\n\nb = 2";
    expect(parseConfig(text)).toEqual({ a: "1", b: "2" });
  });

  test("value containing equals", () => {
    const text = "url = https://example.com?a=b";
    expect(parseConfig(text)).toEqual({ url: "https://example.com?a=b" });
  });

  test("section prefixes keys", () => {
    const text = "[database]\nhost = localhost\nport = 5432";
    expect(parseConfig(text)).toEqual({
      "database.host": "localhost",
      "database.port": "5432",
    });
  });

  test("mixed global and sections", () => {
    const text =
      "app = myapp\n[database]\nhost = localhost\n[cache]\nttl = 300";
    expect(parseConfig(text)).toEqual({
      app: "myapp",
      "database.host": "localhost",
      "cache.ttl": "300",
    });
  });
});

describe("truncate", () => {
  test("short text unchanged", () => {
    expect(truncate("hi", 10)).toBe("hi");
  });

  test("exact length unchanged", () => {
    expect(truncate("hello", 5)).toBe("hello");
  });

  test("long text truncated", () => {
    expect(truncate("hello world", 5)).toBe("hello...");
  });

  test("empty string", () => {
    expect(truncate("", 5)).toBe("");
  });
});
