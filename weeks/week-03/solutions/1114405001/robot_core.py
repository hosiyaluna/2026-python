from dataclasses import dataclass


DIRECTIONS = ["N", "E", "S", "W"]
MOVE_DELTA = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass
class Robot:
    x: int
    y: int
    direction: str
    lost: bool = False


class RobotWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scent = set()

    def create_robot(self, x, y, direction):
        self._validate_position(x, y)
        self._validate_direction(direction)
        return Robot(x=x, y=y, direction=direction)

    def turn_left(self, robot):
        self._ensure_active(robot)
        index = DIRECTIONS.index(robot.direction)
        robot.direction = DIRECTIONS[(index - 1) % 4]
        return robot

    def turn_right(self, robot):
        self._ensure_active(robot)
        index = DIRECTIONS.index(robot.direction)
        robot.direction = DIRECTIONS[(index + 1) % 4]
        return robot

    def step_forward(self, robot):
        self._ensure_active(robot)
        dx, dy = MOVE_DELTA[robot.direction]
        next_x = robot.x + dx
        next_y = robot.y + dy

        if self._in_bounds(next_x, next_y):
            robot.x = next_x
            robot.y = next_y
            return robot

        scent_key = (robot.x, robot.y, robot.direction)
        if scent_key in self.scent:
            return robot

        self.scent.add(scent_key)
        robot.lost = True
        return robot

    def execute(self, robot, commands):
        for command in commands:
            if robot.lost:
                break
            if command == "L":
                self.turn_left(robot)
            elif command == "R":
                self.turn_right(robot)
            elif command == "F":
                self.step_forward(robot)
            else:
                raise ValueError(f"Invalid command: {command}")
        return robot

    def _in_bounds(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height

    def _validate_position(self, x, y):
        if not self._in_bounds(x, y):
            raise ValueError("Robot position out of bounds")

    def _validate_direction(self, direction):
        if direction not in MOVE_DELTA:
            raise ValueError(f"Invalid direction: {direction}")

    @staticmethod
    def _ensure_active(robot):
        if robot.lost:
            raise RuntimeError("Lost robot can no longer move")