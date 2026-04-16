## 解題代碼

```python
def solve():
    line = input().strip()
    # 移除 # 及之後的內容
    equation = line.split('#')[0]
    
    # 七段顯示器編碼 (0-9 的段編碼)
    segments = {
        0: {0, 1, 2, 4, 5, 6},
        1: {2, 5},
        2: {0, 2, 3, 4, 6},
        3: {0, 2, 3, 5, 6},
        4: {1, 2, 3, 5},
        5: {0, 1, 3, 5, 6},
        6: {0, 1, 3, 4, 5, 6},
        7: {0, 2, 5},
        8: {0, 1, 2, 3, 4, 5, 6},
        9: {0, 1, 2, 3, 5, 6}
    }
    
    # 反向查找：從段集合找數字
    def segments_to_digit(segs):
        for digit, seg_set in segments.items():
            if seg_set == segs:
                return digit
        return None
    
    # 解析等式，提取數字位置和值
    def parse_equation(eq):
        parts = eq.split('=')
        if len(parts) != 2:
            return None
        left, right = parts
        return (left, right)
    
    # 計算表達式的值
    def evaluate(expr):
        try:
            # 將表達式中的數字和運算符分離
            result = 0
            current_num = ""
            current_op = "+"
            
            i = 0
            while i < len(expr):
                if expr[i] in "+-":
                    # 處理上一個數字
                    if current_num:
                        if current_op == "+":
                            result += int(current_num)
                        else:
                            result -= int(current_num)
                        current_num = ""
                    
                    # 決定下一個運算符
                    if i == 0 or expr[i-1] in "+-":
                        # 負號
                        current_num = "-"
                    else:
                        current_op = expr[i]
                else:
                    current_num += expr[i]
                i += 1
            
            # 處理最後一個數字
            if current_num:
                if current_op == "+":
                    result += int(current_num)
                else:
                    result -= int(current_num)
            
            return result
        except:
            return None
    
    # 嘗試所有移動
    def try_move(equation):
        left_str, right_str = parse_equation(equation)
        
        # 尋找所有數字及其位置
        def find_numbers(s):
            numbers = []
            i = 0
            while i < len(s):
                if s[i].isdigit() or (s[i] == '-' and i + 1 < len(s) and s[i+1].isdigit()):
                    start = i
                    if s[i] == '-':
                        i += 1
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    numbers.append((start, i, s[start:i]))
                else:
                    i += 1
            return numbers
        
        # 在左邊和右邊都試圖移動
        for side, side_str in [('left', left_str), ('right', right_str)]:
            numbers = find_numbers(side_str)
            
            for start, end, num_str in numbers:
                # 對每個數字的每一位嘗試移除一根木棒
                for digit_pos, digit_char in enumerate(num_str):
                    if not digit_char.isdigit():
                        continue
                    
                    digit = int(digit_char)
                    digit_segs = segments[digit]
                    
                    # 嘗試移除每根木棒
                    for seg in digit_segs:
                        new_segs = digit_segs - {seg}
                        
                        # 嘗試添加每根木棒
                        for add_seg in range(7):
                            test_segs = new_segs | {add_seg}
                            new_digit = segments_to_digit(test_segs)
                            
                            if new_digit is not None:
                                # 構造新數字字符串
                                new_num_str = num_str[:digit_pos] + str(new_digit) + num_str[digit_pos+1:]
                                
                                # 構造新等式
                                if side == 'left':
                                    new_left = side_str[:start] + new_num_str + side_str[end:]
                                    new_eq = new_left + "=" + right_str
                                else:
                                    new_right = side_str[:start] + new_num_str + side_str[end:]
                                    new_eq = left_str + "=" + new_right
                                
                                # 驗證新等式
                                left_val = evaluate(left_str if side == 'left' else new_left if side == 'left' else left_str)
                                right_val = evaluate(right_str if side == 'right' else new_right if side == 'right' else right_str)
                                
                                if side == 'left':
                                    left_val = evaluate(new_left)
                                    right_val = evaluate(right_str)
                                else:
                                    left_val = evaluate(left_str)
                                    right_val = evaluate(new_right)
                                
                                if left_val is not None and right_val is not None and left_val == right_val:
                                    return new_eq
        
        return None
    
    result = try_move(equation)
    if result:
        print(result + "#")
    else:
        print("No")

solve()
```

## 測試用例

*測試輸入與預期輸出*
6-2=0#

8-2=0#