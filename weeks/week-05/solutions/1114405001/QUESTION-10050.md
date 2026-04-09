```python
import sys


def solve() -> None:
	data = list(map(int, sys.stdin.read().split()))
	t = data[0]
	idx = 1
	ans = []

	for _ in range(t):
		n = data[idx]
		idx += 1
		p = data[idx]
		idx += 1

		hartals = data[idx:idx + p]
		idx += p

		lost = [False] * (n + 1)

		for h in hartals:
			day = h
			while day <= n:
				# 第1天是星期天，因此 day%7==6 為星期五，day%7==0 為星期六
				if day % 7 != 6 and day % 7 != 0:
					lost[day] = True
				day += h

		ans.append(str(sum(lost)))

	sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
	solve()
```

## 測試用例

測試輸入：

```text
1
14
3
3
4
8
```

預期輸出：

```text
5
```
