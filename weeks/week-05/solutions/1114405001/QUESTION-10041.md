```python
import sys


def solve() -> None:
	data = list(map(int, sys.stdin.read().split()))
	t = data[0]
	idx = 1
	ans = []

	for _ in range(t):
		r = data[idx]
		idx += 1
		streets = data[idx:idx + r]
		idx += r

		streets.sort()
		median = streets[r // 2]
		total = sum(abs(s - median) for s in streets)
		ans.append(str(total))

	sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
	solve()
```

## 測試用例

測試輸入：

```text
2
2 2 4
3 2 4 6
```

預期輸出：

```text
2
4
```
