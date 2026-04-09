import sys

# 記憶化表，加速計算
memo = {1: 1}

def cycle_length(n):
    original = n
    count = 0

    while n != 1:
        if n in memo:
            count += memo[n]
            memo[original] = count
            return count

        count += 1
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2

    count += 1  # 最後的 1
    memo[original] = count
    return count


for line in sys.stdin:
    if not line.strip():
        continue

    i, j = map(int, line.split())
    low, high = min(i, j), max(i, j)

    max_cycle = 0
    for n in range(low, high + 1):
        max_cycle = max(max_cycle, cycle_length(n))

    print(i, j, max_cycle)