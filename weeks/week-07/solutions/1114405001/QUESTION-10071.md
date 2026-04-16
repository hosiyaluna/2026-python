
## 解題代碼

```python
def solve():
    n = int(input())
    S = []
    for _ in range(n):
        S.append(int(input()))
    
    # 計算所有 2 元素和的頻數
    sum2 = {}
    for i in range(n):
        for j in range(n):
            s = S[i] + S[j]
            sum2[s] = sum2.get(s, 0) + 1
    
    # 計算所有 3 元素和的頻數
    sum3 = {}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                s = S[i] + S[j] + S[k]
                sum3[s] = sum3.get(s, 0) + 1
    
    # 對每個 f，計算滿足 a+b+c+d+e=f 的組合數
    count = 0
    for f in S:
        # 對所有可能的 (a+b) 值，檢查 (c+d+e) = f - (a+b)
        for ab_sum, ab_count in sum2.items():
            cde_sum = f - ab_sum
            if cde_sum in sum3:
                count += ab_count * sum3[cde_sum]
    
    print(count)

solve()
```

## 測試用例

*測試輸入與預期輸出*
1

3
-1
0
1
