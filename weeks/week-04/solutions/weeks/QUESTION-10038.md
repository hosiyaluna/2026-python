# 題目 10038

**題名**: UVA 10038

>
> 【狀態】題目敘述、輸入說明、輸出說明待補充
>
> 【建議】請參考以下連結自行補充：
> - [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a031)
> - [UVA Online Judge](https://uva.onlinejudge.org/external/10038.pdf)
> - [Yui Huang 題解參考](https://yuihuang.com/cpe-level-1/)

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a031)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10038.pdf)

## 題目敘述


有n個整數的序列我們稱為jolly jumper，如果相鄰的2個數其差的絕對值恰好為1到n-1。
例如：1 4 2 3就是jolly jumper（n=4）。
因為相鄰2數的差的絕對值為3,2,1，就是1到n-1。
但是1 4 2 -1 6不是jolly jumper（n=5）。
因為相鄰2數的差的絕對值為3,2,3,7，並非1到n-1。
你的任務是寫一個程式來判斷一個整數序列是否為jolly jumper。

## 輸入說明


每組測試資料一列，第一個正整數為 n（n < 3000），代表此整數序列的長度。
接下來有n個整數，代表此整數序列。
請參考Sample Input。

## 輸出說明


對每一組測試資料，輸出此整數序列是否為jolly jumper。
請參考Sample Output。

---

## 解題思路

這題要判斷一個長度為 `n` 的整數序列，是否滿足：

- 所有相鄰兩數的差的絕對值
- 恰好出現 `1, 2, 3, ..., n-1`

也就是說：

- 差值不能重複
- 差值不能超出 `1` 到 `n-1`
- 最後必須剛好收集到全部 `n-1` 種差值

### 做法

1. 讀入一整列資料
2. 第一個數字是 `n`，後面是這個序列的 `n` 個整數
3. 依序計算相鄰兩數差的絕對值
4. 用集合 `seen` 記錄這些差值
5. 若某個差值不在 `1` 到 `n-1` 之間，就一定不是 Jolly
6. 最後若 `seen` 的大小剛好是 `n-1`，則為 Jolly，否則不是

### 特別情況

當 `n = 1` 時，沒有任何相鄰差值，條件自然成立，所以一定是 `Jolly`。

### 複雜度

對每筆資料只需掃過一次序列，時間複雜度為 `O(n)`。

## 解題代碼

```python
import sys


for line in sys.stdin:
	if not line.strip():
		continue

	nums = list(map(int, line.split()))
	n = nums[0]
	arr = nums[1:]

	if n == 1:
		print("Jolly")
		continue

	seen = set()
	ok = True

	for i in range(1, n):
		diff = abs(arr[i] - arr[i - 1])
		if diff < 1 or diff >= n:
			ok = False
			break
		seen.add(diff)

	if ok and len(seen) == n - 1:
		print("Jolly")
	else:
		print("Not jolly")
```

## 測試用例

**輸入**：

```text
4 1 4 2 3
5 1 4 2 -1 6
1 100
```

**預期輸出**：

```text
Jolly
Not jolly
Jolly
```

**說明**：

- `1 4 2 3` 的相鄰差值為 `3, 2, 1`，剛好是 `1~3`
- `1 4 2 -1 6` 的相鄰差值為 `3, 2, 3, 7`，不符合 `1~4`
- 長度為 `1` 的序列沒有相鄰差值，視為 `Jolly`
