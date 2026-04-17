# 題目 10093

**題名**: UVA 10093

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a086)
- [Yui Huang 題解](https://yuihuang.com/zj-a086/)

## 題目敘述

司令部的將軍們打算在 **N×M 的網格地圖**上部署炮兵部隊。

地圖的每一格可能是：
- **山地**（用 `H` 表示）：不能部署炮兵
- **平原**（用 `P` 表示）：每格最多可部署一支炮兵部隊

一支炮兵部隊的**攻擊範圍**為：沿橫向左右各兩格，沿縱向上下各兩格（攻擊範圍不受地形影響）。

為了**防止誤傷**，任何兩支炮兵部隊之間不能互相攻擊（即任何一支炮兵部隊都不在其他支炮兵部隊的攻擊範圍內）。

請問在整個地圖區域內，**最多能部署多少支炮兵部隊**？

## 輸入說明

- 第一行包含兩個正整數 **N** 和 **M**，以空格分隔（**N ≤ 100，M ≤ 10**）。
- 接下來的 N 行，每行含有連續的 M 個字元（`P` 或 `H`），表示地圖各列的地形。

## 輸出說明

輸出一個整數 **K**，表示最多能部署的炮兵部隊數量。

---

## 解題思路

**Bitmask DP（狀態壓縮）**：

由於 M≤10，每一行的部署方案可用一個 M 位元的 bitmask 表示。  
炮兵攻擊範圍橫向 ±2、縱向 ±2，因此：
- **同行內**：任兩個放置的 bit 距離至少 3（`mask & (mask>>1) == 0` 且 `mask & (mask>>2) == 0`）
- **跨行**：第 i 行與第 i-1 行、第 i-2 行的 bitmask 不能有共同的 1-bit

**DP 狀態設計**：

`dp[prev][pprev]` = 處理完當前行後的最大炮兵數，其中 `prev` = 上一行的 bitmask，`pprev` = 上上行的 bitmask。

**轉移**：對當前行的合法 bitmask `curr`（符合地形且無水平衝突），若 `curr & prev == 0` 且 `curr & pprev == 0`，則：
```
new_dp[curr][prev] = max(dp[prev][pprev]) + popcount(curr)
```

**複雜度分析**：M=10 時合法 bitmask 數量 V=60（由遞推 g(m)=g(m-1)+g(m-3) 得），每行操作 V³=216,000 次，N=100 行共 21,600,000 次，效率充足。

## 解題代碼

```python
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        row = input().strip()
        mask = 0
        for j, c in enumerate(row):
            if c == 'P':
                mask |= (1 << j)
        grid.append(mask)

    # 合法行 bitmask：同行任意兩個 1-bit 距離 >= 3
    valid = [m for m in range(1 << M)
             if not (m & (m >> 1)) and not (m & (m >> 2))]
    V = len(valid)
    vi = {v: i for i, v in enumerate(valid)}

    def popcount(x):
        return bin(x).count('1')

    cnt = [popcount(v) for v in valid]

    # dp[pi][qi] = 目前最大炮兵數（prev=valid[pi], pprev=valid[qi]）
    NEG = -1
    dp = [[NEG] * V for _ in range(V)]

    # 第 0 行初始化（pprev 設為 0，即空行）
    z = vi[0]
    for i, v in enumerate(valid):
        if v & grid[0] == v:   # 所有 1-bit 必須在平原
            dp[i][z] = cnt[i]

    for row_idx in range(1, N):
        terrain = grid[row_idx]
        new_dp = [[NEG] * V for _ in range(V)]
        valid_curr = [(ci, cv) for ci, cv in enumerate(valid)
                      if cv & terrain == cv]

        for ci, cv in valid_curr:
            cc = cnt[ci]
            # 與 curr 相容的 pprev 索引集合（cv & qv == 0）
            compat_q = [qi for qi, qv in enumerate(valid) if not (cv & qv)]
            # 遍歷合法 prev
            for pi, pv in enumerate(valid):
                if cv & pv:
                    continue
                # 在 compat_q 中找 dp[pi][qi] 的最大值
                best = max(dp[pi][qi] for qi in compat_q)
                if best != NEG:
                    new_dp[ci][pi] = best + cc

        dp = new_dp

    ans = max(v for row in dp for v in row if v != NEG)
    print(ans)

main()
```

## 測試用例

**輸入**：
```
5 4
PHPP
PPHH
PPPP
PHPP
PHHP
```

**預期輸出**：
```
6
```

**驗證思路**（M=4，合法 bitmask 共 6 個：0000, 0001, 0010, 0100, 1000, 1001）：

以最優部署示意（`X`=炮兵，`.`=不放）：
```
. X . X    ← 第1行: 1010 = bits 1,3
. . . .    ← 第2行: 0000（山地過多）
X . X .    ← 第3行: 0101 = bits 0,2
. X . .    ← 第4行: 0010 = bit 1
. . . X    ← 第5行: 1000 = bit 3
```
合計 2+0+2+1+1 = **6** ✓
