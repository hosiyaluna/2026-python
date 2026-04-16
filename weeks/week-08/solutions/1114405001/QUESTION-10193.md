# 題目 10193

**題名**: UVA 10193

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a186)
- [Yui Huang 題解](https://yuihuang.com/zj-a186/)

## 題目敘述

**反正切函數**可展開成無窮級數，有如下公式（其中 0 ≤ x ≤ 1）：

$$\arctan(x) = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots$$

使用反正切函數來計算 **π** 是一種常用方法。

例如，最簡單的計算 π 的方式：

$$\pi = 4\arctan(1) = 4\left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots\right)$$

然而這種方法效率很低。利用角度和的正切函數公式：

$$\tan(a+b) = \frac{\tan(a)+\tan(b)}{1-\tan(a)\cdot\tan(b)}$$

可以推導出：

$$\arctan(p) + \arctan(q) = \arctan\!\left(\frac{p+q}{1-pq}\right)$$

例如令 p = 1/2，q = 1/3，則：

$$\arctan\!\left(\frac{1}{2}\right) + \arctan\!\left(\frac{1}{3}\right) = \arctan(1)$$

使用 1/2 和 1/3 的反正切來計算 arctan(1)，速度快得多。

我們將上式寫成如下形式：

$$\arctan\!\left(\frac{1}{a}\right) = \arctan\!\left(\frac{1}{b}\right) + \arctan\!\left(\frac{1}{c}\right)$$

其中 **a、b、c 均為正整數**。

**問題**：對於每一個給定的 a（1 ≤ a ≤ 60000），求 **b + c** 的值。

保證對任意的 a 都存在整數解。若有多個解，要求給出 **b + c 最小**的解。

## 輸入說明

輸入檔案中只有一個正整數 **a**，其中 **1 ≤ a ≤ 60000**。

## 輸出說明

輸出一個整數，為 **b + c** 的值。

---

## 解題思路

使用反正切函數的加法公式：
$$\arctan(p) + \arctan(q) = \arctan\!\left(\frac{p+q}{1-pq}\right)$$

代入 $p = \frac{1}{b}, q = \frac{1}{c}$：

$$\arctan\!\left(\frac{1}{b}\right) + \arctan\!\left(\frac{1}{c}\right) = \arctan\!\left(\frac{b+c}{bc-1}\right)$$

因此需要：
$$\frac{1}{a} = \frac{b+c}{bc-1}$$

交叉相乘：
$$bc - 1 = a(b+c)$$
$$bc - ab - ac = 1$$

重新整理（加 $a^2 - a^2$）：
$$(b-a)(c-a) = a^2 + 1$$

**關鍵洞察**：
- 令 $d_1 = b - a, d_2 = c - a$
- 需要 $d_1 \times d_2 = a^2 + 1$（因數分解）
- 則 $b = a + d_1, c = a + d_2$
- $b + c = 2a + d_1 + d_2$

**最小化策略**：
- 對於固定乘積，當兩個因數最接近時，其和最小
- 因此找最接近 $\sqrt{a^2+1}$ 的因數對
- 從 $i = \lfloor\sqrt{a^2+1}\rfloor$ 往下迭代，找最大的 $i$ 整除 $a^2+1$

## 解題代碼

```python
import math

a = int(input())

# 計算 a² + 1
product = a * a + 1

# 找最接近 √product 的因數對，使得 d1 * d2 = product
# 從大到小找最大的因數
min_sum = float('inf')

for i in range(int(math.sqrt(product)), 0, -1):
    if product % i == 0:
        d1 = i
        d2 = product // i
        current_sum = d1 + d2
        if current_sum < min_sum:
            min_sum = current_sum
        break  # 找到第一個（最大的）因數後即可停止

b = a + d1
c = a + d2

print(b + c)
```

**簡化版本**（同時檢查兩個因數方向）：

```python
a = int(input())
product = a * a + 1

# 找最接近 √product 的因數
best_d1 = 1
best_d2 = product

for i in range(1, int(product**0.5) + 1):
    if product % i == 0:
        d1 = i
        d2 = product // i
        # 更新最小和
        if d1 + d2 < best_d1 + best_d2:
            best_d1 = d1
            best_d2 = d2

b = a + best_d1
c = a + best_d2

print(b + c)
```

## 測試用例

```
輸入:
2

計算過程:
- a = 2，a² + 1 = 5
- 5 的因數對：(1, 5)
- d1 = 1, d2 = 5
- b = 2 + 1 = 3, c = 2 + 5 = 7
- b + c = 10

輸出:
10

驗證:
arctan(1/2) = arctan(1/3) + arctan(1/7)
用加法公式：(1/3 + 1/7)/(1 - 1/21) = (10/21)/(20/21) = 1/2 ✓
```
