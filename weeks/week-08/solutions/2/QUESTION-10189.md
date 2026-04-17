# 題目 10189

**題名**: UVA 10189 — Minesweeper

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a182)
- [Yui Huang 題解](https://yuihuang.com/zj-a182/)

## 題目敘述

你一定玩過 Windows 上的**踩地雷（Minesweeper）**！

遊戲規則如下：
- 在一個 **n 行 m 列**的網格中，某些格子放有**地雷**（以 `*` 表示），其餘格子為空白（以 `.` 表示）。
- 對於每個**空白格子**，需要計算其**周圍 8 個方向**（上、下、左、右、四斜角）中**地雷的數量**，並以該數字填入。

請根據輸入的地雷位置，輸出填好數字的完整地圖。
## 輸入說明

- 輸入包含多組測試資料。
- 每組測試資料第一行為兩個整數 **n** 和 **m**（表示網格的行數和列數）。
- 接下來 n 行，每行 m 個字元（`*` 表示地雷，`.` 表示空白）。
- 以 **n = 0, m = 0** 結束輸入（不需處理）。
## 輸出說明

- 對每組測試資料，先輸出 `Field #X:`（X 為組號，從 1 開始）。
- 地雷格子保持 `*`，空白格子改為周圍 8 格中地雷的數量（0~8 的數字）。
- 每組測試資料之間**輸出一個空行**。

---

## 解題思路

1. **讀取測試資料**：使用迴圈持續讀取 (n, m) 直到遇到 (0, 0)
2. **儲存網格**：將每組測試資料的網格讀入
3. **計算地雷數量**：對於每個空白格子 (`.`)，檢查周圍 8 個方向
4. **輸出結果**：按照格式輸出 `Field #X:` 和修改後的網格
5. **處理空行**：在每組測試資料之間輸出空行（最後一組後不需要）

**八個方向的偏移量**：
- 上、下、左、右：(-1,0), (1,0), (0,-1), (0,1)
- 四個斜角：(-1,-1), (-1,1), (1,-1), (1,1)

## 解題代碼

```python
field_num = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    # 讀取網格
    grid = []
    for _ in range(n):
        grid.append(list(input().strip()))
    
    # 八個方向的偏移量
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    # 處理每個格子
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                # 計算周圍地雷數量
                mine_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                        mine_count += 1
                grid[i][j] = str(mine_count)
    
    # 輸出結果
    print(f"Field #{field_num}:")
    for row in grid:
        print(''.join(row))
    
    field_num += 1
    
    # 在組別之間輸出空行（最後一組時會自動結束，所以每次輸出）
    print()
```

**改進版本**（去掉最後多餘的空行）：

```python
field_num = 1
first = True
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    # 在非第一組前加空行
    if not first:
        print()
    first = False
    
    # 讀取網格
    grid = []
    for _ in range(n):
        grid.append(list(input().strip()))
    
    # 八個方向的偏移量
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    # 處理每個格子
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                # 計算周圍地雷數量
                mine_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '*':
                        mine_count += 1
                grid[i][j] = str(mine_count)
    
    # 輸出結果
    print(f"Field #{field_num}:")
    for row in grid:
        print(''.join(row))
    
    field_num += 1
```

## 測試用例

```
輸入:
4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0

輸出:
Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100
```
