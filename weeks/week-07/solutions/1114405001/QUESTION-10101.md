# 題目 10101

**題名**: UVA 10101

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a094)
- [Yui Huang 題解](https://yuihuang.com/zj-a094/)

## 題目敘述

這是一個很古老的遊戲：用**木棒**在桌上拼出一個**不成立的等式**，移動且只移動**一根木棒**使得等式成立。

現在輪到你了：從輸入讀入一個式子，如果移動一根木棒可以使等式成立，則輸出新的等式，否則輸出 `No`。

**說明與限制：**

1. 式子中只會出現**加號和減號**（包括負號），且有且僅有一個等號。不會出現括號、乘號或除號，也不會有 `++`、`--`、`+-` 或 `-+` 出現。
2. 式子中不會出現 **8 個或 8 個以上的連續數字**。
3. 你只能移動用來構成**數字的木棒**，不能移動構成運算符（`+`、`-`、`=`）的木棒，所以加號、減號、等號不會改變。移動前後，木棒構成的數字必須嚴格符合標準七段顯示器的 0~9。
4. 修改**前**的等式中的數不會以 `0` 開頭，但允許修改**後**的等式中的數以數字 `0` 開頭。

## 輸入說明

從輸入讀入一行字串，該字串包括一個以 **`#`** 字元結尾的式子（ASCII 碼 35）。

- 式子中沒有空格或其他分隔符
- 輸入資料嚴格符合邏輯
- 字串長度 ≤ 1000
- 注意：`#` 字元後面可能有一些與題目無關的字元

## 輸出說明

輸出僅一行：

- 若**有解**，輸出正確的等式，格式與輸入格式相同（以 `#` 結尾，中間不能有分隔符，也不要加入多餘字元）。
- 若**無解**，輸出 `No`（N 大寫，o 小寫）。

---

## 解題思路

**核心思想**：七段顯示器上每個數字 0~9 可用 7-bit bitmask 表示各段是否亮起，移動一根木棒等價於：

- **同位置重排**：從某個數字位置取出一段並放回同位置，即 bitmask 有恰好 2 bits 不同（一個清除、一個新增）。
- **跨位置移動**：從數字 A 移除一段（bitmask 少 1 bit），放到數字 B 增加一段（bitmask 多 1 bit）。

**算法**：

1. 預計算 `same[d]`（同位置重排可達的數字）、`remove[d]`（少一段可達的數字）、`add[d]`（多一段可達的數字）。
2. 解析等式，記錄每個數字在等式中的絕對位置以及其對 `(lhs - rhs)` 的貢獻係數（`±sign × 10^k`），計算當前 `deficit = lhs - rhs`。
3. 枚舉所有合法轉換，若某轉換使 `deficit = 0` 則輸出結果。

**效率優化**：用「每個數字對 deficit 的貢獻係數」將合法性驗證降為 O(1) 純整數運算，避免逐次重新解析字串。

**複雜度**：O(D²)，D 為等式中數字位元數（最多約 500），約 400 萬次整數運算，極快。

**七段顯示器 bitmask（bit 0=頂, 1=右上, 2=右下, 3=底, 4=左下, 5=左上, 6=中）**：

| 數字 | 0  | 1 | 2  | 3  | 4   | 5   | 6   | 7 | 8   | 9   |
|------|-----|---|-----|-----|-----|-----|-----|---|-----|-----|
| mask | 63 | 6 | 91 | 79 | 102 | 109 | 125 | 7 | 127 | 111 |

## 解題代碼

```python
import sys

def main():
    SEG = [63, 6, 91, 79, 102, 109, 125, 7, 127, 111]

    same_t   = [[] for _ in range(10)]
    remove_t = [[] for _ in range(10)]
    add_t    = [[] for _ in range(10)]

    for d in range(10):
        for d2 in range(10):
            xor  = SEG[d] ^ SEG[d2]
            bits = bin(xor).count('1')
            if bits == 2:
                same_t[d].append(d2)
            elif bits == 1:
                if (SEG[d] & SEG[d2]) == SEG[d2]:  # d2 ⊂ d（少一段）
                    remove_t[d].append(d2)
                else:                                # d ⊂ d2（多一段）
                    add_t[d].append(d2)

    def parse_side(s, offset, mult):
        """解析單側算式，返回 (數值, [(絕對位置, 數字值, 貢獻係數)])"""
        val, digs = 0, []
        i, n = 0, len(s)
        while i < n:
            sign = 1
            if s[i] == '+':   sign = 1;  i += 1
            elif s[i] == '-': sign = -1; i += 1
            j = i
            while j < n and s[j].isdigit():
                j += 1
            if j == i:
                return None, None
            val += sign * int(s[i:j])
            length = j - i
            for k in range(length):
                power  = 10 ** (length - 1 - k)
                effect = mult * sign * power      # 對 (lhs - rhs) 的貢獻
                digs.append((offset + i + k, int(s[i+k]), effect))
            i = j
        return val, digs

    for line in sys.stdin:
        line = line.strip()
        hi = line.find('#')
        if hi == -1:
            continue
        eq = line[:hi]
        if not eq:
            continue

        ei = eq.find('=')
        lhs_val, lhs_d = parse_side(eq[:ei],    0,    +1)
        rhs_val, rhs_d = parse_side(eq[ei+1:], ei+1,  -1)

        if lhs_val is None:
            print('No'); continue

        deficit   = lhs_val - rhs_val
        all_digs  = lhs_d + rhs_d  # (abs_pos, digit, effect)
        eq_arr    = list(eq)
        found     = None

        # 情況 1：同位置重排
        for pos, d, eff in all_digs:
            for d2 in same_t[d]:
                if deficit + eff * (d2 - d) == 0:
                    eq_arr[pos] = str(d2)
                    found = ''.join(eq_arr)
                    eq_arr[pos] = str(d)
                    break
            if found: break

        # 情況 2：從 i 移除一段，加到 j
        if not found:
            for i, (pi, di, effi) in enumerate(all_digs):
                if found: break
                for di_new in remove_t[di]:
                    if found: break
                    partial = deficit + effi * (di_new - di)
                    for j, (pj, dj, effj) in enumerate(all_digs):
                        if i == j or found: continue
                        for dj_new in add_t[dj]:
                            if partial + effj * (dj_new - dj) == 0:
                                eq_arr[pi] = str(di_new)
                                eq_arr[pj] = str(dj_new)
                                found = ''.join(eq_arr)
                                break
                        if found: break
                    eq_arr[pi] = str(di)

        print((found + '#') if found else 'No')

main()
```

## 測試用例

**輸入**：
```
1+1=3#
1+1=3+5#
11+77=34#
```

**預期輸出**：
```
1+1=2#
No
17+17=34#
```

**關鍵轉換驗證**：

| 轉換 | SEG 變化 | 合法 |
|------|----------|------|
| 3 → 2（同位置）| 79 → 91，XOR=20（2 bits）| ✓ |
| 7 → 1（少一段）| 7 → 6，XOR=1（1 bit，6⊂7）| ✓ |
| 1 → 7（多一段）| 6 → 7，XOR=1（1 bit，6⊂7）| ✓ |

`11+77=34`：把第2個'1'(pos=1)改為'7'、第1個'7'(pos=3)改為'1'，
效果：lhs 變化 = +6×10 − 6×10 = 0，等式依然成立（17+17=34）✓
