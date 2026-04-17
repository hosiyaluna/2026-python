# 題目 10035

**題名**: UVA 10035

>
> 【狀態】題目敘述、輸入說明、輸出說明待補充
>
> 【建議】請參考以下連結自行補充：
> - [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a028)
> - [UVA Online Judge](https://uva.onlinejudge.org/external/10035.pdf)
> - [Yui Huang 題解參考](https://yuihuang.com/cpe-level-1/)

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a028)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10035.pdf)

## 題目敘述


在小學時我們都做過加法的運算，就是把2個整數靠右對齊然後，由右至左一位一位相加。
如果相加的結果大於等於10就有進位（carry）的情況出現。
你的任務就是要判斷2個整數相加時產生了幾次進位的情況。
這將幫助小學老師分析加法題目的難度。

## 輸入說明


每一列測試資料有2個正整數，長度均小於10位。
最後一列有2個0代表輸入結束。

## 輸出說明


每列測試資料輸出該2數相加時產生多少次進位，請參考Sample Output。
注意進位超過1次時operation有加s

---

## 解題思路

這題就是模擬直式加法。

把兩個整數從**個位數開始**往左一位一位相加，並記錄前一位是否有進位：

- 若 `當前位數字和 + 前一位進位 >= 10`，就會產生一次新的進位
- 否則這一位不會進位

一直做到兩個數字都處理完為止。

### 做法

1. 讀入兩個整數 `a`、`b`
2. 若 `a == 0` 且 `b == 0`，結束輸入
3. 反覆取出個位數：
   - `da = a % 10`
   - `db = b % 10`
4. 計算 `da + db + carry`
5. 若結果大於等於 10：
   - 進位次數加 1
   - `carry = 1`
   否則 `carry = 0`
6. 將 `a //= 10`、`b //= 10` 繼續處理下一位

### 輸出格式

- 0 次進位：`No carry operation.`
- 1 次進位：`1 carry operation.`
- 2 次以上：`x carry operations.`

### 複雜度

若數字長度為 `d`，則每筆資料只需處理 `d` 位，時間複雜度為 `O(d)`。

## 解題代碼

```python
import sys


for line in sys.stdin:
	a, b = map(int, line.split())
	if a == 0 and b == 0:
		break

	carry = 0
	count = 0

	while a > 0 or b > 0:
		total = (a % 10) + (b % 10) + carry
		if total >= 10:
			count += 1
			carry = 1
		else:
			carry = 0
		a //= 10
		b //= 10

	if count == 0:
		print("No carry operation.")
	elif count == 1:
		print("1 carry operation.")
	else:
		print(f"{count} carry operations.")
```

## 測試用例

**輸入**：

```text
123 456
555 555
123 594
0 0
```

**預期輸出**：

```text
No carry operation.
3 carry operations.
1 carry operation.
```

**說明**：

- `123 + 456 = 579`，每一位都沒有進位
- `555 + 555 = 1110`，個位、十位、百位都會進位，共 3 次
- `123 + 594 = 717`，只有十位加法會進位 1 次
