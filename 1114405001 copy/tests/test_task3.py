import unittest

from task3_log_summary import parse_log, summarize_logs


class TestTask3LogSummary(unittest.TestCase):
    def test_parse_log(self):
        self.assertEqual(parse_log("alice login"), ("alice", "login"))

    def test_summarize_logs_basic(self):
        logs = [
            ("alice", "login"),
            ("bob", "login"),
            ("alice", "view"),
            ("alice", "logout"),
            ("bob", "view"),
            ("bob", "view"),
            ("chris", "login"),
            ("bob", "logout"),
        ]
        user_sorted, top_action, top_count = summarize_logs(logs)
        self.assertEqual(user_sorted, [("bob", 4), ("alice", 3), ("chris", 1)])
        self.assertEqual((top_action, top_count), ("login", 3))

    def test_empty_logs(self):
        user_sorted, top_action, top_count = summarize_logs([])
        self.assertEqual(user_sorted, [])
        self.assertEqual(top_action, "NONE")
        self.assertEqual(top_count, 0)


if __name__ == "__main__":
    unittest.main()
