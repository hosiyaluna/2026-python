from dataclasses import replace

from robot_core import RobotWorld


try:
    import pygame
except ImportError:  # pragma: no cover
    pygame = None


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
GRID_SIZE = 80
MARGIN = 60
HUD_X = 600
BG_COLOR = (245, 248, 250)
GRID_COLOR = (170, 180, 190)
ROBOT_COLOR = (37, 99, 235)
LOST_COLOR = (220, 38, 38)
SCENT_COLOR = (234, 179, 8)
TEXT_COLOR = (30, 41, 59)


class RobotGame:
    def __init__(self, width=5, height=3):
        self.world = RobotWorld(width, height)
        self.default_robot = (1, 1, "E")
        self.robot = self.world.create_robot(*self.default_robot)
        self.command_history = []
        self.replay_states = [self._snapshot("Start")]
        self.replay_index = 0
        self.message = "L/R/F 操作，N 新機器人，C 清除 scent，P 回放"

    def reset_robot(self):
        self.robot = self.world.create_robot(*self.default_robot)
        self.command_history = []
        self.replay_states = [self._snapshot("Start")]
        self.replay_index = 0
        self.message = "已建立新機器人（保留 scent）"

    def clear_scent(self):
        self.world.scent.clear()
        self.message = "已清除 scent"
        self.replay_states.append(self._snapshot("Clear scent"))
        self.replay_index = len(self.replay_states) - 1

    def apply_command(self, command):
        if self.robot.lost:
            self.message = "機器人已 LOST，請按 N 建立新機器人"
            return

        before = replace(self.robot)
        self.world.execute(self.robot, command)
        self.command_history.append(command)
        self.replay_states.append(self._snapshot(f"Command {command}"))
        self.replay_index = len(self.replay_states) - 1

        if self.robot.lost:
            self.message = (
                f"{command}: 機器人於 ({before.x}, {before.y}, {before.direction}) 掉落，留下 scent"
            )
        else:
            self.message = (
                f"{command}: ({before.x}, {before.y}, {before.direction}) -> "
                f"({self.robot.x}, {self.robot.y}, {self.robot.direction})"
            )

    def replay_step(self):
        if not self.replay_states:
            return
        self.replay_index = (self.replay_index + 1) % len(self.replay_states)
        label, _, _, _ = self.replay_states[self.replay_index]
        self.message = f"回放：{label}"

    def _snapshot(self, label):
        robot_state = (self.robot.x, self.robot.y, self.robot.direction, self.robot.lost)
        return label, robot_state, sorted(self.world.scent), "".join(self.command_history)


def draw_robot(screen, font, state):
    _, robot_state, scent, history = state
    x, y, direction, lost = robot_state

    grid_x = MARGIN + x * GRID_SIZE + GRID_SIZE // 2
    grid_y = WINDOW_HEIGHT - MARGIN - y * GRID_SIZE - GRID_SIZE // 2
    color = LOST_COLOR if lost else ROBOT_COLOR

    if direction == "N":
        points = [(grid_x, grid_y - 22), (grid_x - 18, grid_y + 18), (grid_x + 18, grid_y + 18)]
    elif direction == "E":
        points = [(grid_x + 22, grid_y), (grid_x - 18, grid_y - 18), (grid_x - 18, grid_y + 18)]
    elif direction == "S":
        points = [(grid_x, grid_y + 22), (grid_x - 18, grid_y - 18), (grid_x + 18, grid_y - 18)]
    else:
        points = [(grid_x - 22, grid_y), (grid_x + 18, grid_y - 18), (grid_x + 18, grid_y + 18)]

    pygame.draw.polygon(screen, color, points)
    screen.blit(font.render(f"指令歷史: {history}", True, TEXT_COLOR), (HUD_X, 290))

    for sx, sy, _ in scent:
        px = MARGIN + sx * GRID_SIZE + GRID_SIZE // 2
        py = WINDOW_HEIGHT - MARGIN - sy * GRID_SIZE - GRID_SIZE // 2
        pygame.draw.circle(screen, SCENT_COLOR, (px, py), 8)


def draw_board(screen, font, game):
    screen.fill(BG_COLOR)
    width = game.world.width
    height = game.world.height

    for col in range(width + 2):
        x = MARGIN + col * GRID_SIZE
        pygame.draw.line(screen, GRID_COLOR, (x, MARGIN), (x, WINDOW_HEIGHT - MARGIN), 1)

    for row in range(height + 2):
        y = MARGIN + row * GRID_SIZE
        pygame.draw.line(screen, GRID_COLOR, (MARGIN, y), (MARGIN + (width + 1) * GRID_SIZE, y), 1)

    for col in range(width + 1):
        screen.blit(font.render(str(col), True, TEXT_COLOR), (MARGIN + col * GRID_SIZE + 28, WINDOW_HEIGHT - 42))

    for row in range(height + 1):
        screen.blit(font.render(str(row), True, TEXT_COLOR), (22, WINDOW_HEIGHT - MARGIN - row * GRID_SIZE - 12))

    snapshot = game.replay_states[game.replay_index]
    label, robot_state, scent, _ = snapshot
    draw_robot(screen, font, snapshot)

    status_text = (
        f"位置: ({robot_state[0]}, {robot_state[1]}) 方向: {robot_state[2]} "
        f"狀態: {'LOST' if robot_state[3] else 'ALIVE'}"
    )
    screen.blit(font.render("Robot Lost 視覺化", True, TEXT_COLOR), (HUD_X, 80))
    screen.blit(font.render(status_text, True, TEXT_COLOR), (HUD_X, 130))
    screen.blit(font.render(f"scent: {scent}", True, TEXT_COLOR), (HUD_X, 170))
    screen.blit(font.render(f"快照: {label}", True, TEXT_COLOR), (HUD_X, 210))
    screen.blit(font.render(game.message, True, TEXT_COLOR), (HUD_X, 250))

    help_lines = [
        "操作鍵:",
        "L / R / F 逐步操作",
        "N 建立新機器人",
        "C 清除 scent",
        "P 切換回放快照",
        "ESC 離開",
    ]
    for index, text in enumerate(help_lines):
        screen.blit(font.render(text, True, TEXT_COLOR), (HUD_X, 350 + index * 34))


def main():
    if pygame is None:
        raise SystemExit("請先安裝 pygame：pip install pygame")

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Robot Lost")
    font = pygame.font.SysFont("microsoftjhengheiui", 24)
    clock = pygame.time.Clock()
    game = RobotGame()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_n:
                    game.reset_robot()
                elif event.key == pygame.K_c:
                    game.clear_scent()
                elif event.key == pygame.K_p:
                    game.replay_step()
                elif event.unicode.upper() in {"L", "R", "F"}:
                    game.apply_command(event.unicode.upper())

        draw_board(screen, font, game)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()