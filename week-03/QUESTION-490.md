import sys

lines = [line.rstrip("\n") for line in sys.stdin]

if not lines:
    exit()

max_len = max(len(line) for line in lines)

# 補齊每行到相同長度
padded = [line.ljust(max_len) for line in lines]

# 旋轉 90 度（順時針）
for col in range(max_len):
    out = []
    for row in range(len(padded) - 1, -1, -1):
        out.append(padded[row][col])
    print("".join(out))