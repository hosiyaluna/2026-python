import unittest

from task2_student_ranking import parse_student, rank_students, top_k_students


class TestTask2StudentRanking(unittest.TestCase):
    def test_parse_student(self):
        self.assertEqual(
            parse_student("amy 88 20"),
            {"name": "amy", "score": 88, "age": 20},
        )

    def test_ranking_tie_break(self):
        students = [
            {"name": "amy", "score": 88, "age": 20},
            {"name": "bob", "score": 88, "age": 19},
            {"name": "zoe", "score": 92, "age": 21},
            {"name": "eva", "score": 92, "age": 20},
            {"name": "ian", "score": 88, "age": 19},
        ]
        ranked = rank_students(students)
        self.assertEqual([s["name"] for s in ranked], ["eva", "zoe", "bob", "ian", "amy"])

    def test_top_k_exceeds_length(self):
        students = [{"name": "leo", "score": 75, "age": 20}]
        self.assertEqual(top_k_students(students, 3), students)


if __name__ == "__main__":
    unittest.main()
