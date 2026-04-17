# 題目 10170

**題名**: UVA 10170 — The Hotel with Infinite Rooms

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a163)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10170.pdf)

## 題目敘述

HaluaRuti 城裡有一家奇特的旅館，擁有**無限多間房間**。

旅館的住宿規則如下：

- 同一時間只能有**一個旅行團**住宿。
- 每個旅行團**早上入住，傍晚退房**。
- 前一個旅行團退房的**隔天早上**，下一個旅行團入住。
- **每個旅行團的人數比前一個多 1 人**（起始旅行團除外，其人數為 S）。
- 一個有 **n 人**的旅行團，會住 **n 天**。

例如：若起始旅行團有 4 人，則第 1~4 天住 4 人團，第 5~9 天住 5 人團，以此類推。

給定起始旅行團的人數 **S** 和查詢天數 **D**，請找出**第 D 天住宿的旅行團有幾人**。

## 輸入說明

- 每行包含兩個整數 **S**（1 ≤ S ≤ 10000）和 **D**（1 ≤ D < 10¹⁵）。
- 所有輸入和輸出整數均小於 10¹⁵。
- 輸入直到 **EOF** 結束。

## 輸出說明

每行輸入對應一行輸出，為**第 D 天住宿的旅行團人數**。

---

## 解題思路

**數學推導**：

設第 0 個旅行團有 S 人（住 S 天），第 1 個有 S+1 人，…，第 k 個（0-indexed）有 S+k 人、住 S+k 天。

前 k 組（索引 0 到 k-1）共佔用的總天數：

$$\text{cum}(k) = \sum_{i=0}^{k-1}(S+i) = kS + \frac{k(k-1)}{2}$$

要找第 D 天屬於哪一組，等價於找**最小的 k**（表示「前 k 組結束」的累計天數）使得 $\text{cum}(k) \geq D$，  
答案即為該組的人數 $S + (k-1)$。

**二分搜**：

- 搜尋範圍：$k \in [1,\ \sqrt{2D} + S]$
- $D < 10^{15}$，因此 $k_{\max} \approx \sqrt{2 \times 10^{15}} \approx 4.5 \times 10^7$，二分搜 O(log k) ≈ 47 次，極快。

## 解題代碼

```python
import sys
import math

def solve(S, D):
    # 二分搜：最小 k 使得 k*S + k*(k-1)//2 >= D
    lo, hi = 1, 2 * int(math.isqrt(2 * D)) + S + 2
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * S + mid * (mid - 1) // 2 >= D:
            hi = mid
        else:
            lo = mid + 1
    # 第 D 天屬於第 lo-1 組（0-indexed），人數為 S + (lo-1)
    return S + lo - 1

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 2:
        continue
    S, D = int(parts[0]), int(parts[1])
    print(solve(S, D))
```

## 測試用例

**輸入**：
```
4 1
4 4
4 5
4 9
4 10
1 1000000000000000
```

**預期輸出**：
```
4
4
5
5
6
1414213563
```

**手動驗證（S=4）**：

| 旅行團（0-indexed） | 人數 | 佔用天數範圍 |
|---|---|---|
| 0 | 4 | 1 – 4 |
| 1 | 5 | 5 – 9 |
| 2 | 6 | 10 – 15 |

- D=1 → 4 ✓  
- D=4 → 4 ✓  
- D=5 → 5 ✓  
- D=9 → 5 ✓  
- D=10 → 6 ✓
