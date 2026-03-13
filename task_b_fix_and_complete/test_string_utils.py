import unittest
from string_utils import parse_config, truncate


class TestParseConfig(unittest.TestCase):
    def test_simple_pairs(self):
        text = "name = Alice\nage = 30"
        self.assertEqual(parse_config(text), {'name': 'Alice', 'age': '30'})

    def test_comments_ignored(self):
        text = "# This is a comment\nkey = value"
        self.assertEqual(parse_config(text), {'key': 'value'})

    def test_empty_lines_ignored(self):
        text = "a = 1\n\n\nb = 2"
        self.assertEqual(parse_config(text), {'a': '1', 'b': '2'})

    def test_value_containing_equals(self):
        """Values can contain '=' characters — e.g. URLs with query strings."""
        text = "url = https://example.com?a=b"
        self.assertEqual(parse_config(text), {'url': 'https://example.com?a=b'})

    def test_section_prefixes_keys(self):
        """Keys inside a [section] should be prefixed with 'section.'"""
        text = "[database]\nhost = localhost\nport = 5432"
        self.assertEqual(parse_config(text), {
            'database.host': 'localhost',
            'database.port': '5432'
        })

    def test_mixed_global_and_sections(self):
        """Keys before any section have no prefix; keys inside sections are prefixed."""
        text = "app = myapp\n[database]\nhost = localhost\n[cache]\nttl = 300"
        self.assertEqual(parse_config(text), {
            'app': 'myapp',
            'database.host': 'localhost',
            'cache.ttl': '300'
        })


class TestTruncate(unittest.TestCase):
    def test_short_text_unchanged(self):
        self.assertEqual(truncate("hi", 10), "hi")

    def test_exact_length_unchanged(self):
        self.assertEqual(truncate("hello", 5), "hello")

    def test_long_text_truncated(self):
        self.assertEqual(truncate("hello world", 5), "hello...")

    def test_empty_string(self):
        self.assertEqual(truncate("", 5), "")


if __name__ == "__main__":
    unittest.main()
