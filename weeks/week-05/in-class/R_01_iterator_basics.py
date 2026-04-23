# Remember（記憶）- 迭代器基礎概念

# 1. 迭代器協議的核心方法
# Python 的 for 迴圈本質上就是反覆呼叫 next()，
# 直到拿到 StopIteration 為止。
# 所謂「迭代器協議」可先記兩件事：
# 1) iter(obj) 取得迭代器（會呼叫 obj.__iter__()）
# 2) next(it) 取得下一筆（會呼叫 it.__next__()）
items = [1, 2, 3]

# iter() 呼叫 __iter__()
it = iter(items)
print(f"迭代器: {it}")

# next() 呼叫 __next__()
# 每呼叫一次 next(it)，游標就往前移一格。
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 沒有更多元素時，擲出 StopIteration
# 這個例外不是錯誤情況，而是「正常結束訊號」。
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
# 「可迭代物件」= 可以丟進 for 迴圈的東西。
print("\n--- 常見可迭代物件 ---")

# 列表
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串
print(f"字串 iter: {iter('abc')}")

# 字典
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案
import io

# 真實檔案物件與 StringIO 都可逐行迭代；
# for line in file 的背後也是迭代器機制。
f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件
# 這裡把「資料容器」與「走訪狀態」拆成兩個類別：
# - CountDown：可迭代物件（負責產生迭代器）
# - CountDownIterator：迭代器（負責記錄目前走到哪）
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 每次 for 重新開始時都建立新的迭代器，
        # 這樣同一個 CountDown 物件可被重跑。
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        # 倒數到 0 以前都回傳值，0 之後結束。
        if self.current <= 0:
            raise StopIteration
        # 先遞減再回傳，是為了輸出 start, start-1, ..., 1
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表是可迭代物件，不是迭代器
# 重點差異：
# - 可迭代物件：可被 iter() 轉成迭代器
# - 迭代器：可被 next() 連續取值，且有狀態前進
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 列表的 iter() 返回迭代器
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身就是可迭代物件
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")


# 手動遍歷（章節 4.1 風格）
# 這段等價於 for item in items: ...
# 只是把 for 的內部機制明確寫出來。
def manual_iter(items):
    it = iter(items)
    while True:
        try:
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            # 沒資料時跳出 while True
            break


manual_iter(["a", "b", "c"])


# 使用預設值的版本
# next(it, 預設值) 可避免 try/except，
# 當迭代結束時直接回傳預設值。
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 預設值
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
