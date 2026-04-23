# Understand（理解）- itertools 工具函數

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")


def count(n):
    # 簡易無限計數器生成器：從 n 開始一直往上加。
    # 因為是生成器，不會一次把無限資料放進記憶體。
    i = n
    while True:
        yield i
        i += 1


c = count(0)
# islice(iterable, start, stop) 可對「迭代器」做切片，
# 很適合無限序列或不想先轉 list 的情境。
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")

print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
# dropwhile(predicate, iterable)：
# - 會從前面開始「一直丟棄」符合條件的元素
# - 一旦遇到第一個不符合條件的元素，後面就全部保留（不再判斷跳過）
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

print("\n--- takewhile() 條件取用 ---")
# takewhile(predicate, iterable)：
# - 從前面開始「一直取用」符合條件的元素
# - 一旦遇到第一個不符合條件的元素就立刻停止
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

print("\n--- chain() 串聯 ---")
# chain(a, b, c) 可把多個可迭代物件視為一個連續序列。
# 優點是惰性處理，不需先做 a + b + c 產生中間清單。
a = [1, 2]
b = [3, 4]
c = [5]
print(f"chain(a, b, c): {list(chain(a, b, c))}")

print("\n--- permutations() 排列 ---")
# permutations：排列，重視順序，且預設不重複取同一元素。
items = ["a", "b", "c"]
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

# r=2 代表從 items 取 2 個做有序排列。
print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

print("\n--- combinations() 組合 ---")
# combinations：組合，不重視順序。
# ('a','b') 與 ('b','a') 視為同一組，不會重複出現。
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
# 這裡用 permutations(chars, 2)：
# - 長度為 2
# - 元素不可重複
# - 順序不同視為不同密碼
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement

# combinations_with_replacement：可重複取元素，但仍是「組合」概念，
# 所以 AB 與 BA 不會同時出現。
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")
