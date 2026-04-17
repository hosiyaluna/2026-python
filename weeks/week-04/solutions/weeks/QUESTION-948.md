# 題目 948

**題名**: UVA 948

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=c095)
- [Yui Huang 題解](https://yuihuang.com/zj-c095/)

## 題目敘述


「金條」銀行根據可靠消息，他們的最後一批（有N個）硬幣裡有一個是假的，而且它的重量和真的不同（每個真的硬幣都一樣重）。
在金融危機之後，他們只剩下如上圖的天平。
那個天平能用來確定左邊盤子裡的東西比右邊的重、輕、還是一樣。
為了找出假幣，銀行職員把所有的硬幣編號（從 1 到 N ），然後他們就開始秤重了。
他們每次都把左右放一樣多的硬幣，然後記錄硬幣的編號以及秤重結果。
你要寫一個程式幫他們找出假的硬幣。

## 輸入說明


輸入的第一列有一個整數 M，代表以下有幾組測試資料。
每組測試資料的第一列有2個整數 N 和 K。
N 代表硬幣的數量（1 <= N <= 100），K 是秤重的次數（1 <= K <= 100）。
接下來的 2K 列描述秤重，每連續的2列是一次秤重。
前一列開始有一個數Pi（1 <= Pi <= N/2），代表這次秤重每邊放的硬幣個數，接下來的前 Pi個數字是左邊的硬幣號碼，後 Pi 個數字是右邊的硬幣號碼。
後一列用 <, >, 或 = 表示秤重的結果。
< 表示左邊比右邊的輕> 表示左邊比右邊的重= 表示兩邊一樣重輸入的第一列與第一組測試資料，以及各組測試資料間均有一空白列。
請參考Sample Input。

## 輸出說明


對每一組測試資料輸出哪一個硬幣是假的。
如果秤重的結果無法找出假幣，請輸出 0。
測試資料間亦請輸出一空白列，請參考Sample Output。

---

## 解題思路

這題可以直接**枚舉假幣是誰**，並分成兩種情況檢查：

- 該硬幣比真幣重
- 該硬幣比真幣輕

如果某顆硬幣在其中任一種假設下，能讓**所有秤重結果都成立**，那它就是可能的假幣。

最後：

- 如果只有 **1 顆**硬幣可能是假幣，輸出它的編號
- 如果有 **0 顆或超過 1 顆**都可能，代表無法唯一判定，輸出 `0`

### 如何檢查一個假設是否成立

假設第 `x` 顆硬幣是假幣：

- 若假設它比較重：
  - 在左盤會讓左邊變重
  - 在右盤會讓右邊變重
- 若假設它比較輕：
  - 在左盤會讓左邊變輕
  - 在右盤會讓右邊變輕
- 若 `x` 不在這次秤重中，結果必須是 `=`

把每次秤重都驗證一次即可。

### 複雜度

共有 `N` 顆硬幣，每顆檢查「重 / 輕」兩種狀態；每種狀態驗證 `K` 次秤重。

時間複雜度為 `O(NK)`，在 `N, K <= 100` 下非常輕鬆。

## 解題代碼

```python
import sys


def possible(coin, heavier, weighings):
	for left, right, result in weighings:
		if coin in left:
			actual = '>' if heavier else '<'
		elif coin in right:
			actual = '<' if heavier else '>'
		else:
			actual = '='

		if actual != result:
			return False
	return True


def main():
	tokens = sys.stdin.read().split()
	if not tokens:
		return

	idx = 0
	cases = int(tokens[idx])
	idx += 1
	answers = []

	for _ in range(cases):
		n = int(tokens[idx])
		k = int(tokens[idx + 1])
		idx += 2

		weighings = []
		for _ in range(k):
			p = int(tokens[idx])
			idx += 1
			left = set(map(int, tokens[idx:idx + p]))
			idx += p
			right = set(map(int, tokens[idx:idx + p]))
			idx += p
			result = tokens[idx]
			idx += 1
			weighings.append((left, right, result))

		candidates = []
		for coin in range(1, n + 1):
			if possible(coin, True, weighings) or possible(coin, False, weighings):
				candidates.append(coin)

		answers.append(str(candidates[0] if len(candidates) == 1 else 0))

	print('\n\n'.join(answers))


main()
```

## 測試用例

**輸入**：

```text
2

5 3
2 1 2 3 4
<
1 1 4
=
1 2 5
=

4 2
1 1 2
<
1 3 4
=
```

**預期輸出**：

```text
3

0
```

**說明**：

- 第一組中，只有第 `3` 顆硬幣能符合全部秤重結果
- 第二組中，可能情況不只一種，無法唯一判定，因此輸出 `0`
