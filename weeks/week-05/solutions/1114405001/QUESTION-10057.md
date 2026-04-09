```python
import sys
from bisect import bisect_left, bisect_right


def solve() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	idx = 0
	out = []

	while idx < len(data):
		n = data[idx]
		idx += 1
		arr = data[idx:idx + n]
		idx += n

		arr.sort()
		low = arr[(n - 1) // 2]
		high = arr[n // 2]

		left_pos = bisect_left(arr, low)
		right_pos = bisect_right(arr, high)
		count = right_pos - left_pos
		ways = high - low + 1

		out.append(f"{low} {count} {ways}")

	sys.stdout.write("\n".join(out))


if __name__ == "__main__":
	solve()
```

## 測試用例

測試輸入：

```text
5
1 2 3 4 5
4
1 2 2 3
```

預期輸出：

```text
3 1 1
2 2 1
```
