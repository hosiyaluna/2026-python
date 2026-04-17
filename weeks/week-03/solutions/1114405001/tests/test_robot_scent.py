import unittest

from robot_core import RobotWorld


class RobotScentTests(unittest.TestCase):
    def setUp(self):
        self.world = RobotWorld(5, 3)

    def test_first_lost_robot_leaves_scent(self):
        robot = self.world.create_robot(5, 3, "N")
        self.world.step_forward(robot)
        self.assertIn((5, 3, "N"), self.world.scent)

    def test_second_robot_ignores_dangerous_forward_with_same_scent(self):
        first = self.world.create_robot(5, 3, "N")
        self.world.step_forward(first)

        second = self.world.create_robot(5, 3, "N")
        self.world.step_forward(second)

        self.assertEqual((5, 3, "N", False), (second.x, second.y, second.direction, second.lost))

    def test_same_cell_different_direction_does_not_share_scent(self):
        first = self.world.create_robot(5, 3, "N")
        self.world.step_forward(first)

        second = self.world.create_robot(5, 3, "E")
        self.world.step_forward(second)

        self.assertTrue(second.lost)
        self.assertIn((5, 3, "E"), self.world.scent)

    def test_execute_with_scent_continues_following_commands(self):
        first = self.world.create_robot(5, 3, "N")
        self.world.execute(first, "F")

        second = self.world.create_robot(5, 3, "N")
        self.world.execute(second, "FRF")

        self.assertEqual((5, 3, "E", True), (second.x, second.y, second.direction, second.lost))
        self.assertIn((5, 3, "E"), self.world.scent)

    def test_sample_case_robot_one_matches_uva_118(self):
        robot = self.world.create_robot(1, 1, "E")
        self.world.execute(robot, "RFRFRFRF")
        self.assertEqual((1, 1, "E", False), (robot.x, robot.y, robot.direction, robot.lost))

    def test_sample_case_robot_two_matches_uva_118(self):
        robot = self.world.create_robot(3, 2, "N")
        self.world.execute(robot, "FRRFLLFFRRFLL")
        self.assertEqual((3, 3, "N", True), (robot.x, robot.y, robot.direction, robot.lost))

    def test_sample_case_robot_three_uses_existing_scent(self):
        lost_robot = self.world.create_robot(3, 2, "N")
        self.world.execute(lost_robot, "FRRFLLFFRRFLL")

        robot = self.world.create_robot(0, 3, "W")
        self.world.execute(robot, "LLFFFLFLFL")
        self.assertEqual((2, 3, "S", False), (robot.x, robot.y, robot.direction, robot.lost))


if __name__ == "__main__":
    unittest.main()