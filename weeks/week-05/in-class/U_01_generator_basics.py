# Understand（理解）- 生成器概念


def frange(start, stop, step):
    # frange: float range 的示範版本。
    # 與一次建立完整清單相比，生成器會「需要時才產生下一個值」。
    x = start
    while x < stop:
        # yield 會把目前值送出去，並暫停函式狀態；
        # 下一次被 next() 呼叫時，會從這行後面繼續執行。
        yield x
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    # 這個範例用來觀察生成器何時執行：
    # 建立生成器物件時不會立刻跑函式本體，
    # 直到第一次 next() 才開始執行。
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    # 當 while 結束、函式自然返回時，外部 next() 會收到 StopIteration。
    print("Done!")


print("\n--- 建立生成器 ---")
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
# 每次 next(c) 取一個值，生成器狀態就往前推進一次。
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    next(c)
except StopIteration:
    # 生成器沒有值可產生時，拋出 StopIteration（正常結束訊號）。
    print("StopIteration!")


def fibonacci():
    # 無限序列生成器：理論上可一直產生下去。
    # 典型用法是外部搭配 for/range/itertools.islice 控制取值數量。
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
for i in range(10):
    # 這裡只取前 10 項，避免無限迴圈。
    print(next(fib), end=" ")
print()


def chain_iter(*iterables):
    # 把多個可迭代物件串接成一個連續序列。
    for it in iterables:
        # yield from 可把子迭代器的元素逐一轉交出去，
        # 比手動 for x in it: yield x 更精簡。
        yield from it


print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        # 讓 Node 可被 for 走訪其子節點。
        return iter(self.children)

    def depth_first(self):
        # 深度優先（DFS）前序遍歷：
        # 先回傳自己，再遞迴走訪每個子樹。
        yield self
        for child in self:
            yield from child.depth_first()


print("\n--- 樹的深度優先遍歷 ---")
root = Node(0)
root.add_child(Node(1))
root.add_child(Node(2))
root.children[0].add_child(Node(3))
root.children[0].add_child(Node(4))

for node in root.depth_first():
    print(node.value, end=" ")
print()


def flatten(items):
    # 遞迴攤平巢狀可迭代物件。
    for x in items:
        # 若元素本身可迭代（且不是字串），就遞迴展開。
        # 特別排除 str，避免把字串拆成單一字元。
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
