# 題目 10071

**題名**: UVA 10071

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a064)
- [Yui Huang 題解](https://yuihuang.com/zj-a064/)

## 題目敘述

給定一個整數集合 S，其元素均介於 -30000 到 30000 之間（含首尾）。
請計算满足条件的六元組數量：a + b + c + d + e = f，其中 a、b、c、d、e、f 均屬於 S（可重複使用）。

## 輸入說明

第一行包含一個整數 N（1 ≤ N ≤ 100），代表集合 S 的元素個數。
接下來的 N 行，每行一個整數，為 S 的元素。
所有數字均不重複。

## 輸出說明

輸出符合條件的六元組總數量。

---

## 解題思路

**真正的公式**（ZeroJudge 頁面以圖片顯示）為：**(a+b)×c = d + e×f**，其中 a, b, c, d, e, f 均屬於集合 S（可重複選取）。

**Meet-in-the-Middle 策略**：

1. 枚舉所有有序三元組 (a, b, c)，計算左側 `(a+b)*c` 的值並以 Counter 記錄各值出現次數。
2. 枚舉所有有序三元組 (d, e, f)，計算右側 `d + e*f`，查表累加匹配次數。

- 時間複雜度：O(N³)，N≤100 → 最多 10⁶ 次操作，完全可行。
- 多筆測資以空白行分隔，使用 `split()` 整批讀入即可正確解析。

## 解題代碼

```python
import sys
from collections import Counter

def solve():
    data = sys.stdin.read().split()
    idx = 0
    results = []

    while idx < len(data):
        N = int(data[idx]); idx += 1
        S = []
        for _ in range(N):
            S.append(int(data[idx])); idx += 1

        # 左側：(a+b)*c
        lhs = Counter()
        for a in S:
            for b in S:
                ab = a + b
                for c in S:
                    lhs[ab * c] += 1

        # 右側：d + e*f，查左側 Counter 累加
        count = 0
        for e in S:
            for f in S:
                ef = e * f
                for d in S:
                    count += lhs[d + ef]

        results.append(count)

    print('\n\n'.join(map(str, results)))

solve()
```

## 測試用例

**輸入**：
```
1
1

2
2
3

2
-1
1

3
5
7
10
```

**預期輸出**：
```
1

4

24

10
```

**手動驗證 S={-1,1}**：

左側 `(a+b)*c` 的分佈：
- -2 → 2 種（a+b=-2, c=1 或 a+b=2, c=-1）
- 0 → 4 種
- 2 → 2 種

右側 `d+e*f` 分佈相同。

答案 = 2² + 4² + 2² = **24** ✓
