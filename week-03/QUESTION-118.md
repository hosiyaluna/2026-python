import sys

# 方向順序：左轉 -1，右轉 +1
dirs = ["N", "E", "S", "W"]
move = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0)
}

# scent: 記錄掉落前的位置與方向
scent = set()

# 讀取地圖大小
first = True
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    if first:
        max_x, max_y = map(int, line.split())
        first = False
        continue

    # 讀取機器人初始位置
    x, y, d = line.split()
    x = int(x)
    y = int(y)

    # 讀取指令
    commands = sys.stdin.readline().strip()

    lost = False

    for c in commands:
        if c == "L":
            d = dirs[(dirs.index(d) - 1) % 4]
        elif c == "R":
            d = dirs[(dirs.index(d) + 1) % 4]
        else:  # F
            dx, dy = move[d]
            nx, ny = x + dx, y + dy

            # 準備掉落
            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                # 若這個位置 + 方向已經有 scent → 忽略
                if (x, y, d) in scent:
                    continue
                else:
                    # 留下 scent
                    scent.add((x, y, d))
                    lost = True
                    break
            else:
                x, y = nx, ny

    if lost:
        print(x, y, d, "LOST")
    else:
        print(x, y, d)