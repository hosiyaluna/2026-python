# Remember（記憶）- enumerate() 和 zip()

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate(iterable) 會回傳 (索引, 值) 的配對，
# 可避免自己手動維護計數器 i += 1。
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# start=1 常用在「第幾項」的人類編號情境，
# 讓顯示從 1 開始，而不是預設的 0。
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# 實務上常見：搭配檔案逐行讀取時標示行號，
# 有助於除錯或輸出錯誤訊息（第幾行格式錯誤）。
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
# zip(a, b) 會把兩個序列「對位打包」成 (a_i, b_i)。
# 非常適合平行走訪多個序列。
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
# zip 不只兩個，三個以上序列也可以同時對位。
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# 重要：zip 會以「最短序列」為準，多出的元素會被忽略。
x = [1, 2]
y = ["a", "b", "c"]
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# 若不想丟失較長序列的資料，可用 zip_longest，
# 並用 fillvalue 補齊缺少的位置。
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
# 常見技巧：用 zip 將 keys 與 values 配對後轉成 dict。
# 前提是兩者順序一一對應。
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
d = dict(zip(keys, values))
print(f"dict: {d}")
