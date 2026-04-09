```python
import sys


class Fenwick:
	def __init__(self, n: int) -> None:
		self.n = n
		self.bit = [0] * (n + 1)

	def add(self, idx: int, delta: int) -> None:
		while idx <= self.n:
			self.bit[idx] += delta
			idx += idx & -idx

	def prefix_sum(self, idx: int) -> int:
		res = 0
		while idx > 0:
			res += self.bit[idx]
			idx -= idx & -idx
		return res

	def range_sum(self, left: int, right: int) -> int:
		return self.prefix_sum(right) - self.prefix_sum(left - 1)


def solve() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	idx = 0
	n = data[idx]
	idx += 1
	q = data[idx]
	idx += 1

	bit = Fenwick(n)
	state = [0] * (n + 1)  # 0: 增函數, 1: 減函數
	ans = []

	for _ in range(q):
		v = data[idx]
		idx += 1

		if v == 1:
			i = data[idx]
			idx += 1
			if state[i] == 0:
				state[i] = 1
				bit.add(i, 1)
			else:
				state[i] = 0
				bit.add(i, -1)
		else:
			left = data[idx]
			idx += 1
			right = data[idx]
			idx += 1
			cnt = bit.range_sum(left, right)
			ans.append("1" if cnt % 2 == 1 else "0")

	sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
	solve()
```

## 測試用例

測試輸入：

```text
5 7
2 1 5
1 3
2 1 5
1 5
2 3 5
1 3
2 1 5
```

預期輸出：

```text
0
1
0
1
```
