# Task C: Implement from Spec

Open `student_summary.py` and implement the function described below. A test file is provided.

**Running the tests:** Open a terminal in this folder and run:
```
python -m pytest test_student_summary.py -v
```
All 4 tests should pass when you're done.

## The Function

Write a function called `summarize_scores` that takes a list of student records and returns a summary grouped by subject.

Each student record is a dictionary with three keys: `name` (str), `subject` (str), and `score` (int or float).

The function should return a dictionary where each key is a subject name, and each value is a dictionary with:
- `"average"` — the average score for that subject (as a float)
- `"top_scorer"` — the name of the student with the highest score in that subject

If two students tie for top score in a subject, return whichever one appears first in the input list.

---

## Example 1

**Input:**
```python
records = [
    {"name": "Alice", "subject": "Math", "score": 90},
    {"name": "Bob", "subject": "Math", "score": 80},
    {"name": "Alice", "subject": "English", "score": 85},
    {"name": "Bob", "subject": "English", "score": 95},
]
```

**Output:**
```python
{
    "Math": {"average": 85.0, "top_scorer": "Alice"},
    "English": {"average": 90.0, "top_scorer": "Bob"},
}
```

---

## Example 2

**Input:**
```python
records = [
    {"name": "Charlie", "subject": "Science", "score": 72},
]
```

**Output:**
```python
{
    "Science": {"average": 72.0, "top_scorer": "Charlie"},
}
```
