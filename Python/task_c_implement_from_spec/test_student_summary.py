import unittest
from student_summary import summarize_scores


class TestSummarizeScores(unittest.TestCase):
    def test_two_subjects(self):
        records = [
            {"name": "Alice", "subject": "Math", "score": 90},
            {"name": "Bob", "subject": "Math", "score": 80},
            {"name": "Alice", "subject": "English", "score": 85},
            {"name": "Bob", "subject": "English", "score": 95},
        ]
        result = summarize_scores(records)
        self.assertEqual(result["Math"]["average"], 85.0)
        self.assertEqual(result["Math"]["top_scorer"], "Alice")
        self.assertEqual(result["English"]["average"], 90.0)
        self.assertEqual(result["English"]["top_scorer"], "Bob")

    def test_single_record(self):
        records = [
            {"name": "Charlie", "subject": "Science", "score": 72},
        ]
        result = summarize_scores(records)
        self.assertEqual(result["Science"]["average"], 72.0)
        self.assertEqual(result["Science"]["top_scorer"], "Charlie")

    def test_three_students_one_subject(self):
        records = [
            {"name": "Alice", "subject": "Math", "score": 70},
            {"name": "Bob", "subject": "Math", "score": 90},
            {"name": "Charlie", "subject": "Math", "score": 80},
        ]
        result = summarize_scores(records)
        self.assertEqual(result["Math"]["average"], 80.0)
        self.assertEqual(result["Math"]["top_scorer"], "Bob")

    def test_tied_scores_returns_first(self):
        records = [
            {"name": "Alice", "subject": "Art", "score": 95},
            {"name": "Bob", "subject": "Art", "score": 95},
        ]
        result = summarize_scores(records)
        self.assertEqual(result["Art"]["average"], 95.0)
        self.assertEqual(result["Art"]["top_scorer"], "Alice")


if __name__ == "__main__":
    unittest.main()
