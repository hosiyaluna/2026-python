import unittest

from task1_sequence_clean import (
    parse_input,
    dedupe_keep_order,
    sort_ascending,
    sort_descending,
    filter_evens,
)


class TestTask1SequenceClean(unittest.TestCase):
    def test_parse_input_normal(self):
        self.assertEqual(parse_input("5 3 5 2 9 2 8 3 1"), [5, 3, 5, 2, 9, 2, 8, 3, 1])

    def test_dedupe_keep_order(self):
        data = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        self.assertEqual(dedupe_keep_order(data), [5, 3, 2, 9, 8, 1])

    def test_sort_both_directions(self):
        data = [5, 3, 5, 2, 9, 2, 8, 3, 1]
        self.assertEqual(sort_ascending(data), [1, 2, 2, 3, 3, 5, 5, 8, 9])
        self.assertEqual(sort_descending(data), [9, 8, 5, 5, 3, 3, 2, 2, 1])

    def test_filter_evens_with_negatives(self):
        data = [7, -4, 0, 9, 2, 11]
        self.assertEqual(filter_evens(data), [-4, 0, 2])


if __name__ == "__main__":
    unittest.main()
