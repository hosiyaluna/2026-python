import sys

open_quote = True  # True 表示下一個 " 要變成 ``

for line in sys.stdin:
    line = list(line)  # 轉成 list 方便修改
    for i, ch in enumerate(line):
        if ch == '"':
            if open_quote:
                line[i] = "``"
            else:
                line[i] = "''"
            open_quote = not open_quote
    print("".join(line), end="")