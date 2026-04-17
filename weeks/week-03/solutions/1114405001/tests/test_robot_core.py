import unittest

from robot_core import RobotWorld


class RobotCoreTests(unittest.TestCase):
    def setUp(self):
        self.world = RobotWorld(5, 3)

    def test_turn_left_from_north_to_west(self):
        robot = self.world.create_robot(1, 1, "N")
        self.world.turn_left(robot)
        self.assertEqual("W", robot.direction)

    def test_turn_right_from_north_to_east(self):
        robot = self.world.create_robot(1, 1, "N")
        self.world.turn_right(robot)
        self.assertEqual("E", robot.direction)

    def test_four_right_turns_restore_direction(self):
        robot = self.world.create_robot(1, 1, "S")
        self.world.execute(robot, "RRRR")
        self.assertEqual("S", robot.direction)

    def test_forward_inside_boundary_moves_robot(self):
        robot = self.world.create_robot(1, 1, "E")
        self.world.step_forward(robot)
        self.assertEqual((2, 1, False), (robot.x, robot.y, robot.lost))

    def test_forward_out_of_boundary_marks_lost(self):
        robot = self.world.create_robot(5, 3, "N")
        self.world.step_forward(robot)
        self.assertTrue(robot.lost)
        self.assertEqual((5, 3), (robot.x, robot.y))

    def test_lost_robot_stops_executing_later_commands(self):
        robot = self.world.create_robot(5, 3, "N")
        self.world.execute(robot, "FRF")
        self.assertEqual((5, 3, "N", True), (robot.x, robot.y, robot.direction, robot.lost))

    def test_invalid_command_raises_value_error(self):
        robot = self.world.create_robot(0, 0, "N")
        with self.assertRaises(ValueError):
            self.world.execute(robot, "X")

    def test_invalid_direction_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.world.create_robot(0, 0, "A")
