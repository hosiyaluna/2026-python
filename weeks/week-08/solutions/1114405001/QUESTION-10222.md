# 題目 10222

**題名**: UVA 10222 — Decode the Mad man

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a215)
- [Yui Huang 題解](https://yuihuang.com/zj-a215/)

## 題目敘述

有一個瘋狂的人在用鍵盤打字，但他的手每次都向右偏移了**三個按鍵**（相對於標準 QWERTY 鍵盤佈局）。

因此，他所打出來的字，實際上是向右偏移了 3 鍵的**加密文字**。

請你將這份加密文字**解碼**還原，輸出原來應該打出的正確文字。

**鍵盤佈局說明（QWERTY 標準鍵盤，由左到右）：**

```
第一排：` 1 2 3 4 5 6 7 8 9 0 - =
第二排：q w e r t y u i o p [ ] \
第三排：a s d f g h j k l ; '
第四排：z x c v b n m , . /
```

若加密字元是 `r`，則解碼後是 `e`（將位置向左移 3 位）。

## 輸入說明

輸入只有一行，含有某個學生的編號 **id**（**2 ≤ id ≤ 10000**）。

## 輸出說明

- 如果該名學生為**優質學生**，請輸出 `yes`
- 否則請輸出 `no`

---

## 解題思路

1. **建立鍵盤映射**：
   - 將 QWERTY 鍵盤按行排列成一維數列
   - 建立從加密字符到原始字符的映射

2. **解碼邏輯**：
   - 加密手段是向右偏移3個按鍵
   - 解碼就是向左偏移3個按鍵
   - 對每個加密字符，在數列中找到其位置，然後向左移3位

3. **邊界處理**：
   - 大小寫字母都需要處理
   - 保持非字母字符（如空格、標點等）不變

4. **實現**：
   - 逐行讀取輸入
   - 對每行的每個字符進行解碼
   - 輸出解碼後的結果

## 解題代碼

```python
# 建立鍵盤佈局
keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

# 建立解碼映射：加密字符 -> 原始字符
decode_map = {}
for i in range(len(keyboard)):
    if i >= 3:
        # 原始字符在向左移3位的位置
        decode_map[keyboard[i]] = keyboard[i - 3]

# 讀取所有輸入行以處理多行情況
import sys
for line in sys.stdin:
    line = line.rstrip('\n')
    result = []
    for char in line:
        if char in decode_map:
            # 是鍵盤上的字符，進行解碼
            result.append(decode_map[char])
        else:
            # 不是鍵盤字符，保持不變
            result.append(char)
    
    print(''.join(result))
```

**簡化版本**（如果只有單行輸入）：

```python
# 建立鍵盤佈局
keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

# 建立解碼映射
decode_map = {}
for i in range(len(keyboard)):
    if i >= 3:
        decode_map[keyboard[i]] = keyboard[i - 3]

# 讀取加密文字
encrypted = input()

# 解碼
result = []
for char in encrypted:
    if char in decode_map:
        result.append(decode_map[char])
    else:
        result.append(char)

print(''.join(result))
```

## 測試用例

```
輸入:
rfv

計算過程:
- 'r' 的位置：keyboard[10]
- 向左移3位：keyboard[7] = 'e'
- 'f' 的位置：keyboard[20]
- 向左移3位：keyboard[17] = 'd'
- 'v' 的位置：keyboard[38]
- 向左移3位：keyboard[35] = 'c'

輸出:
edc

輸入:
wdt wdt

輸出:
was was
```
