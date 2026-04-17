# 題目 299

**題名**: UVA 299

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=e561)
- [Yui Huang 題解](https://yuihuang.com/zj-e561/)

## 題目敘述


在老舊的火車站，您也許會遇到少數僅存的"車箱置換員"。
"車箱置換員"是鐵路部門的員工，主要工作就是重新排列火車車廂。
一旦以最佳順序排列了車廂，所有火車司機要做的就是將車廂逐一卸下即可。
"車箱置換員"源自在鐵路橋附近的車站中執行此任務的第一人。
這座橋並不會垂直打開，而是繞著河中央的一根支柱旋轉。
將橋旋轉90度後，船隻就能向左或向右駛過。
第一位"車箱置換員"發現，這座橋最多可以在其上運行兩個車廂，通過將橋旋轉180度，車廂就能切換位置。
(缺點是車廂面向相反的方向，但是火車車廂可以以任何一種方式移動，所以沒差）。
現在幾乎所有的"車箱置換員"都已經淘汰了，鐵路公司希望將其操作自動化。
你的任務就是寫一個程式，該程式要計算最少需要交換幾次兩個相鄰車廂，才能將所有車廂依序排好。

## 輸入說明


輸入的第一行包含一個整數N，N代表測資數量。
每組測資的第一行包含一個整數L (0 ≤ L ≤ 50)，L代表火車的長度。
第二行包含數字1到L的排列，表示火車車廂的當前順序。
需要將火車車廂依照編號1到L的順序排好。

## 輸出說明

對於每組測資，請輸出："Optimal train swapping takes S swaps."，S代表最少交換次數。

---

## 解題思路

題目要求的是：

- 每次只能交換**相鄰**的兩個車廂
- 問最少需要幾次交換，才能把序列排成遞增順序

這正好就是序列中的 **逆序對（inversion）數量**。

### 為什麼逆序對數量就是答案？

若有兩個車廂 `a[i] > a[j]` 且 `i < j`，代表這一對順序顛倒了。
因為每次只能交換相鄰車廂，所以要讓這一對恢復正確順序，至少需要一次相鄰交換把它們跨過去。

因此：

- 每個逆序對都必須被修正一次
- 最少交換次數 = 逆序對總數

### 做法

由於 `L <= 50` 很小，可以直接用兩層迴圈統計逆序對：

- 枚舉所有 `i < j`
- 若 `arr[i] > arr[j]`，就把答案加 1

### 複雜度

每筆資料的時間複雜度是 `O(L^2)`，在 `L <= 50` 下非常輕鬆。

## 解題代碼

```python
import sys


t = int(sys.stdin.readline())

for _ in range(t):
	length = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))

	swaps = 0
	for i in range(length):
		for j in range(i + 1, length):
			if arr[i] > arr[j]:
				swaps += 1

	print(f"Optimal train swapping takes {swaps} swaps.")
```

## 測試用例

**輸入**：

```text
3
3
1 3 2
4
4 3 2 1
5
1 2 3 4 5
```

**預期輸出**：

```text
Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 0 swaps.
```

**說明**：

- `1 3 2` 只有 `(3,2)` 這一組逆序對，所以需要 1 次交換
- `4 3 2 1` 是完全反序，共有 `4*3/2 = 6` 個逆序對
- 已排序序列不需要任何交換
