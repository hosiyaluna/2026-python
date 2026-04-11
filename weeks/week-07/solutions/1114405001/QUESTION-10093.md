## 解題代碼

```python
def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input().strip())
    
    # 預處理：獲取每一行可部署炮兵的位置
    def get_valid_states(row):
        """返回該行所有合法的部署狀態"""
        valid = []
        # 枚舉所有可能的子集
        for mask in range(1 << m):
            # 檢查是否都是平原
            ok = True
            for col in range(m):
                if (mask & (1 << col)) and grid[row][col] != 'P':
                    ok = False
                    break
            if not ok:
                continue
            
            # 檢查同一行內是否互相攻擊
            conflict = False
            for col1 in range(m):
                if not (mask & (1 << col1)):
                    continue
                for col2 in range(col1 + 1, m):
                    if not (mask & (1 << col2)):
                        continue
                    # 檢查兩個炮兵距離
                    if col2 - col1 <= 2:  # 橫向距離 ≤ 2
                        conflict = True
                        break
                if conflict:
                    break
            
            if not conflict:
                valid.append(mask)
        
        return valid
    
    def can_coexist(row1, state1, row2, state2):
        """檢查兩行的狀態是否兼容"""
        for col1 in range(m):
            if not (state1 & (1 << col1)):
                continue
            for col2 in range(m):
                if not (state2 & (1 << col2)):
                    continue
                # 檢查縱向距離
                if abs(row1 - row2) <= 2:
                    # 橫向距離
                    if abs(col1 - col2) <= 2:
                        return False
        return True
    
    # 獲取所有行的合法狀態
    all_states = []
    for row in range(n):
        all_states.append(get_valid_states(row))
    
    # DP
    if n == 0:
        print(0)
        return
    
    # dp[i][s] = 前 i 行，第 i 行狀態為 s 時的最大部署數
    dp = [{} for _ in range(n)]
    
    # 初始化第 0 行
    for state in all_states[0]:
        dp[0][state] = bin(state).count('1')
    
    # 逐行轉移
    for row in range(1, n):
        for state in all_states[row]:
            max_val = 0
            # 從前一行的所有合法狀態轉移
            for prev_state in dp[row - 1]:
                if can_coexist(row - 1, prev_state, row, state):
                    max_val = max(max_val, dp[row - 1][prev_state])
            
            if max_val > 0 or row == 1:  # 初始化為 0 或前面有解
                dp[row][state] = max_val + bin(state).count('1')
    
    # 找最大值
    result = 0
    if dp[n - 1]:
        result = max(dp[n - 1].values())
    
    print(result)

solve()
```

## 測試用例

*測試輸入與預期輸出*
4 4
PPPP
PPPP
PPPP
PPPP

8