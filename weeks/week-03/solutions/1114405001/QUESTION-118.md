# 題目 118

**題名**: UVA 118

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=c082)
- [Yui Huang 題解](https://yuihuang.com/zj-c082/)

## 題目敘述


給你一塊矩形土地的長寬，再依序給定每個機器人的初始位置狀況及一連串的指令集，你必須用你的程式求出每個機器人最後的位置狀況。
一個機器人的位置狀況包括了其坐標（ x 坐標， y 坐標），和它面向的方向（用 N , S , E , W 來分別代表北、南、東、西）。
至於一個機器人所收到的指令集，是一個由字母 ' L ' ， ' R ' ， 和 ' F ' 所構成的字串，其分別代表：左轉（Left）：機器人在原地往左轉 90 度。
右轉（Right）: 機器人在原地往右轉 90 度。
前進（Forward）: 機器人往其面向的方向向前走一格，且不改變其面向之方向。
從坐標 (x,y) 走至 (x,y+1) 的這個方向我們定義為北方。
因為此矩形土地是有邊界的，所以一旦一個機器人走出邊界掉落下去，就相當於永遠消失了。
不過這個掉下去的機器人會留下「標記 ( scent ) 」，提醒以後的機器人，避免他們從同一個地方掉下去。
掉下去的機器人會把標記，留在他掉落之前所在的最後一個坐標點。
所以對於以後的機器人，當他正位在有標記的地方時，這個機器人就會忽略會讓他掉下去的指令。

## 輸入說明


輸入裡的第一列有2個正整數，代表這個矩形世界右上角頂點的坐標，其中假設這個世界的左下角頂點坐標為 ( 0 , 0 )。
接下來是若干組有關機器人的初始位置狀況和指令集，每個機器人2列。
第一列為位置狀況，包括了兩個整數和一個字元（ N , S , E 或 W ），代表機器人初始的位置坐標以及機器人最初所面對的方向。
第二列則是指令集，是一個由 ' L ' ， ' R ' 和 ' F ' 所組成的字串。
輸入以 end-of-file 作為結束。
各機器人是依序動作的，也就是說，直到一個機器人作完他全部的動作，下一個機器人才會開始動作。
所有機器人的初始位置皆會在矩形土地上，不會落在外面。
任何坐標的最大值皆不會超過 50 。
每個指令集的長度皆不會超過 100 個字元長。

## 輸出說明


對於每一個機器人，你都必須輸出其最後所在的坐標和面對的方向。
如果一個機器人會掉落出此世界外，你必須先輸出他在掉落前，最後的所在位置和面對的方向，再多加一個字： LOST 。

---

## 解題思路

這題是純模擬題，重點在 `scent` 規則。

### 核心概念

每台機器人依序執行指令：

- `L`：左轉 90 度
- `R`：右轉 90 度
- `F`：朝目前方向前進一格

如果執行 `F` 後會走出邊界：

- 若目前位置與方向 `(x, y, dir)` **沒有**留下過 `scent`
  - 這台機器人會 `LOST`
  - 在 `(x, y, dir)` 留下一筆 `scent`
  - 後續指令不再執行
- 若 `(x, y, dir)` **已經有** `scent`
  - 代表以前有機器人從這裡、朝這個方向掉下去過
  - 這次的 `F` 直接忽略，機器人不移動，也不會 `LOST`

### 資料結構

- 方向陣列：`['N', 'E', 'S', 'W']`
- 位移表：
  - `N -> (0, 1)`
  - `E -> (1, 0)`
  - `S -> (0, -1)`
  - `W -> (-1, 0)`
- `scent` 用集合 `set()` 儲存三元組 `(x, y, dir)`

### 複雜度

若共有 `R` 台機器人、每台最多 `L` 個指令，則時間複雜度為 `O(RL)`。

## 解題代碼

```python
import sys


directions = ['N', 'E', 'S', 'W']
move = {
	'N': (0, 1),
	'E': (1, 0),
	'S': (0, -1),
	'W': (-1, 0),
}


def turn_left(direction):
	index = directions.index(direction)
	return directions[(index - 1) % 4]


def turn_right(direction):
	index = directions.index(direction)
	return directions[(index + 1) % 4]


lines = [line.strip() for line in sys.stdin if line.strip()]
if lines:
	max_x, max_y = map(int, lines[0].split())
	scent = set()

	index = 1
	while index + 1 < len(lines):
		x, y, direction = lines[index].split()
		x = int(x)
		y = int(y)
		commands = lines[index + 1]
		index += 2

		lost = False

		for command in commands:
			if command == 'L':
				direction = turn_left(direction)
			elif command == 'R':
				direction = turn_right(direction)
			else:
				dx, dy = move[direction]
				next_x = x + dx
				next_y = y + dy

				if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
					x, y = next_x, next_y
				else:
					key = (x, y, direction)
					if key in scent:
						continue
					scent.add(key)
					lost = True
					break

		if lost:
			print(x, y, direction, 'LOST')
		else:
			print(x, y, direction)
```

## 測試用例

**輸入**：

```text
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
```

**預期輸出**：

```text
1 1 E
3 3 N LOST
2 3 S
```

**說明**：

- 第 2 台機器人從 `(3, 3)` 朝北前進會掉出邊界，因此留下 `scent = (3, 3, 'N')`
- 第 3 台機器人之後走到同樣的 `(3, 3, 'N')` 時，危險的 `F` 會被忽略，因此不會掉下去
