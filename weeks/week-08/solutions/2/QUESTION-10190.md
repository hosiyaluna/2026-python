# 題目 10190

**題名**: UVA 10190

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a183)
- [Yui Huang 題解](https://yuihuang.com/zj-a183/)

## 題目敘述

M 國是個多雨的國家，尤其是 P 城，頻繁的降雨給人們的出行帶來了很多麻煩。

為了方便行人雨天過馬路，有關部門在每處人行橫道的上空都安裝了一種名為「**自動傘**」的裝置。每把自動傘都可以近似看作一塊**長方形的板**（厚度不計），具有相當出色的吸水能力——落到傘上的雨水會完全被傘頂的小孔吸入，並通過管道排走。

**自動傘的運作方式：**

- 不下雨時，傘閒置。
- 一旦下雨，傘便以**均速直線往返運動**：從馬路一邊移動到另一邊，再返回，如此往復，直到雨停。
- 任何時刻，自動傘都不會越過馬路邊界。

由於單把傘大小有限，主要人行橫道上空安裝了**多把自動傘**。每把傘的寬度等於人行橫道寬度，但長度和移動速率各不相同。

以馬路**左邊界為原點**，向右為 x 軸正方向，建立平面直角坐標系，每把傘可看作平面上的一條**線段**。

請計算從開始下雨到 **T 秒後**，一共有多少**體積**的雨水落到人行橫道上。

## 輸入說明

第一行有四個整數 **N、W、T、V**：
- **N**：自動傘的數目
- **W**：馬路的寬度
- **T**：統計時間長度（秒）
- **V**：單位面積單位時間內的降雨體積

接下來的 N 行，每行用三個整數描述一把自動傘：
- **x**：傘的初始位置（左端點的橫坐標）
- **l**：傘的長度（x 方向的尺寸）
- **v**：傘的速度（v > 0 向右移動；v < 0 向左移動；v = 0 靜止不動）

## 輸出說明

輸出一個實數，表示從開始下雨到 T 秒後，落到人行橫道上的**雨水總體積**，結果**精確到小數點後第二位**。

---

## 解題思路

1. **問題理解**：
   - 傘會收集落在其上的雨水
   - 需要計算**落到地面上**（未被傘覆蓋）的雨水體積
   - 而非被傘收集的體積

2. **核心思路**：
   - 計算每把傘在T秒內「掃過」的x方向範圍
   - 傘在[0, W-l]範圍內往返運動
   - 建立所有傘的覆蓋範圍**並集**
   - 未覆蓋長度 = W - 並集長度
   - 雨水體積 = 未覆蓋長度 × W × V

3. **傘的覆蓋計算**：
   - 對每把傘模擬其往返運動
   - 追蹤傘左端點的最小和最大位置
   - 傘覆蓋的x範圍 = [min位置, max位置 + l]

4. **區間並集**：
   - 將所有傘的覆蓋區間進行排序和合併

## 解題代碼

```python
def get_umbrella_coverage(x, l, v, W, T):
    """
    計算傘在T秒內覆蓋的x範圍（左端點的最小和最大值）
    返回 (min_pos, max_pos + l)
    """
    if v == 0:
        # 靜止不動
        return (x, x + l)
    
    boundary_min = 0
    boundary_max = W - l
    
    # 確保初始位置在有效範圍內
    pos = max(boundary_min, min(x, boundary_max))
    
    vel = v
    min_pos = pos
    max_pos = pos
    
    # 模擬運動，追蹤位置極值
    time = 0
    dt = 0.001  # 時間步長
    
    while time < T:
        dt = min(dt, T - time)
        pos += vel * dt
        time += dt
        
        # 邊界檢查和反彈
        if pos <= boundary_min:
            pos = boundary_min
            vel = abs(vel)  # 向右反彈
        elif pos >= boundary_max:
            pos = boundary_max
            vel = -abs(vel)  # 向左反彈
        
        min_pos = min(min_pos, pos)
        max_pos = max(max_pos, pos)
    
    # 傘的覆蓋範圍
    return (min_pos, max_pos + l)


def merge_intervals(intervals):
    """
    將區間進行合併，返回合併後的總長度
    """
    if not intervals:
        return 0
    
    intervals.sort()
    total_length = 0
    start, end = intervals[0]
    
    for s, e in intervals[1:]:
        if s <= end:
            # 區間重疊，擴展
            end = max(end, e)
        else:
            # 區間不重疊，累加
            total_length += end - start
            start, end = s, e
    
    # 最後一個區間
    total_length += end - start
    return total_length


# 主程式
N, W, T, V = map(int, input().split())

intervals = []
for _ in range(N):
    x, l, v = map(int, input().split())
    # 計算傘的覆蓋範圍
    coverage = get_umbrella_coverage(x, l, v, W, T)
    # 只記錄在有效範圍內的部分
    if coverage[0] < W and coverage[1] > 0:
        coverage = (max(0, coverage[0]), min(W, coverage[1]))
        intervals.append(coverage)

# 計算被伞覆蓋的總長度
covered_length = merge_intervals(intervals)

# 未被覆蓋的長度
uncovered_length = W - covered_length

# 雨水體積 = 未覆蓋區域 × 寬度 × 降雨量 × 時間
# = uncovered_length × W × V × T
rainfall_volume = uncovered_length * W * V

# 精確到小數點後第二位
print(f"{rainfall_volume:.2f}")
```

## 測試用例

```
輸入:
2 10 10 1
0 3 1
5 2 -1

輸出:
(需根據實際情況計算)
```

**說明**：
- 第一把傘：初始位置0，長度3，速度1（向右），會逐漸向右運動
- 第二把傘：初始位置5，長度2，速度-1（向左），會逐漸向左運動
- 寬度W=10，時間T=10秒，降雨量V=1
- 計算兩把傘覆蓋的區間並集，然後計算未覆蓋區域的雨水體積
