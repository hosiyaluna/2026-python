# 題目 10008

**題名**: UVA 10008

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a001)
- [Yui Huang 題解](https://yuihuang.com/zj-a001/)

## 題目敘述

**密碼翻譯（cryptanalysis）** 是指把某個人寫的密文（cryptographic writing）加以分解，這個過程通常會對密文訊息做**統計分析**。

你的任務就是寫一個程式來對密文作簡單的分析。

## 輸入說明

- 第 1 列有一個正整數 **n**，代表以下有多少列需要分析的密文。
- 接下來的 n 列，每列含有 0 或多個字元（可能包含空白字元）。

## 輸出說明

每列包含一個**大寫字元**（A~Z）和一個**正整數**（該字元在輸入中出現的次數）：

- 輸入中大小寫（例如：A 及 a）視為**相同的字元**。
- 輸出時請按照字元出現**次數由大到小**排列。
- 若有 2 個以上字元出現次數相同，則按照**字元字母順序**（例如：A 在 H 之前）由小到大排列。
- 若某一字元**未出現**在輸入中，則不應出現在輸出中。

---

## 解題思路

這題只需要做兩件事：

1. 把所有英文字母出現次數統計起來
2. 依照題目要求排序輸出

### 統計方式

- 逐行讀入文字
- 只處理英文字母 `A` 到 `Z`、`a` 到 `z`
- 先轉成大寫，讓大小寫視為同一個字母
- 用字典或陣列累計次數

### 排序規則

題目要求：

- 次數多的排前面
- 若次數相同，字母小的排前面

因此排序鍵可以寫成：

- 第一關鍵字：`-count`
- 第二關鍵字：`letter`

### 複雜度

假設總字元數為 `L`：

- 統計次數是 `O(L)`
- 排序最多只排 26 個字母，是 `O(26 log 26)`，可視為常數

所以總時間複雜度是 `O(L)`。

## 解題代碼

```python
from collections import Counter


n = int(input())
counter = Counter()

for _ in range(n):
	line = input()
	for ch in line:
		if ch.isalpha():
			counter[ch.upper()] += 1

items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))

for letter, count in items:
	print(letter, count)
```

## 測試用例

**輸入**：

```text
3
This is a test.
Count me 1 2 3 4 5.
Wow!!!! Is this question easy?
```

**預期輸出**：

```text
S 7
T 6
I 5
E 4
O 3
A 2
H 2
U 2
W 2
C 1
M 1
N 1
Q 1
Y 1
```

**說明**：

- `s` 和 `S` 要合併計算
- 數字、空白、標點符號都要忽略
- 輸出時只列出有出現過的英文字母