# 題目 490

**題名**: UVA 490

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=c045)
- [Yui Huang 題解](https://yuihuang.com/zj-c045/)

## 題目敘述

這題要你把輸入的文字矩陣**順時針旋轉 90 度**後輸出。

原本的文字是按照：

- 由左到右
- 由上到下

排列；旋轉之後，會變成：

- 由上到下
- 由右到左

也就是說：

- 原本的**最後一行**會變成輸出的**最左邊一列**
- 原本的**第一行**會變成輸出的**最右邊一列**

例如輸入兩行：

```text
HELLO
WORLD
```

旋轉後就要按照新的方向重新輸出。

## 輸入說明

輸入包含多行文字，直到 EOF 結束。

- 最多不超過 100 行
- 每行最多不超過 100 個字元
- 合法字元包含：空白、標點符號、數字、大小寫英文字母
- `Tab` 不會出現在輸入中

## 輸出說明

請將整個輸入視為一個文字矩陣，輸出其**順時針旋轉 90 度**後的結果。

輸出時需注意：

- 輸入的最後一行要出現在輸出的最左側
- 輸入的第一行要出現在輸出的最右側
- 若某些行長度較短，必須補上適當的空白，讓旋轉後的版面正確

換句話說，應先把所有輸入行視為一個以最長列為寬度的矩形，再進行旋轉輸出。

## 解題思路

這題要把整個文字矩陣**順時針旋轉 90 度**。

### 觀察

假設輸入共有 `n` 行，最長的一行長度為 `m`。

如果先把所有輸入補成一個 `n × m` 的矩形，旋轉後：

- 輸出的第 `col` 行
- 會由原本矩陣中「從下到上」的第 `col` 欄組成

也就是說：

- 外層枚舉原矩陣的每一欄 `col = 0 ... m-1`
- 內層從最後一列往第一列掃描
- 依序取出 `lines[row][col]`

### 細節

由於每一行長度可能不同：

- 如果某一行沒有第 `col` 個字元，就要補空白

所以最簡單的做法是：

1. 先讀入所有行
2. 找出最長行長 `max_len`
3. 對每一行用 `ljust(max_len)` 補空白
4. 依照旋轉規則輸出

### 複雜度

若共有 `n` 行、最長長度為 `m`，則時間複雜度為 `O(nm)`。

## 解題代碼

```python
import sys


lines = [line.rstrip('\n') for line in sys.stdin]

if lines:
		max_len = max(len(line) for line in lines)
		padded = [line.ljust(max_len) for line in lines]

		for col in range(max_len):
				result = []
				for row in range(len(padded) - 1, -1, -1):
						result.append(padded[row][col])
				print(''.join(result).rstrip())
```

## 測試用例

**輸入**：

```text
Rene Decartes once said,
"I think, therefore I am."
```

**預期輸出**：

```text
"R
Ie
	n
t e
h D
i e
n c
k a
, r
	t
t e
h s
e  
r o
e n
f c
o e
r  
e s
	a
I i
	d
a ,
m"
```

**補充測試**：

**輸入**：

```text
HELLO
WORLD
```

**預期輸出**：

```text
WH
OE
RL
LL
DO
```
