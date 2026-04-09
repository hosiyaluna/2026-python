import sys

def solve():
    for line in sys.stdin:
        if not line.strip():
            continue
        parts = list(map(int, line.split()))
        n = parts[0]
        nums = parts[1:]

        if n == 1:
            print("Jolly")
            continue

        diffs = set()
        for i in range(1, n):
            d = abs(nums[i] - nums[i - 1])
            if 1 <= d <= n - 1:
                diffs.add(d)
            else:
                # 差值超出範圍，直接判定不是 jolly
                diffs.add(-1) 
                break

        if len(diffs) == n - 1 and -1 not in diffs:
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == "__main__":
    solve()