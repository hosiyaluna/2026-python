```python
import sys


def solve() -> None:
	data = sys.stdin.read().strip().split()
	if not data:
		return

	s = int(data[0])
	idx = 1
	ans = []

	for _ in range(s):
		n = int(data[idx])
		idx += 1
		p = float(data[idx])
		idx += 1
		i = int(data[idx])
		idx += 1

		if p == 0.0:
			prob = 0.0
		else:
			q = 1.0 - p
			numerator = (q ** (i - 1)) * p
			denominator = 1.0 - (q ** n)
			prob = numerator / denominator

		ans.append(f"{prob:.4f}")

	sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
	solve()
```

## 測試用例

測試輸入：

```text
3
3 0.1666667 2
3 0.5 1
4 0 3
```

預期輸出：

```text
0.2857
0.5714
0.0000
```
