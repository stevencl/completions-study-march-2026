# Task B: Complete and Implement

You have a module `string_utils.py` with two functions and a test file `test_string_utils.py`.

**Your task:** Run the tests, read the output, and make all tests pass.

## Steps

1. Run the tests:
   ```
   python -m pytest test_string_utils.py -v
   ```

2. Read the output — some tests pass, some fail. The failing tests show you what's missing.

3. Complete the TODO in `parse_config()` and implement the missing `truncate()` function.

## What the functions should do

- **`parse_config(text)`** — Parses a multi-line key=value config string into a dictionary. Most of it already works (comments, empty lines, basic key=value pairs). What's missing: **section support**. Lines like `[database]` are section headers, and keys inside a section should be prefixed — e.g., `host` becomes `database.host`. Keys before any section header have no prefix.

- **`truncate(text, max_length)`** — If the text is longer than `max_length` characters, cut it to `max_length` characters and append `"..."`. If the text is already within `max_length`, return it unchanged. An empty string should be returned unchanged.
