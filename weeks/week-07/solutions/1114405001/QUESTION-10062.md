## 解題代碼

```python
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.build(1, 1, n)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = 1
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
    
    def update(self, node, start, end, idx):
        if start == end:
            self.tree[node] = 0
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node, start, mid, idx)
            else:
                self.update(2 * node + 1, mid + 1, end, idx)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
    
    def query(self, node, start, end, k):
        if start == end:
            return start
        mid = (start + end) // 2
        if self.tree[2 * node] >= k:
            return self.query(2 * node, start, mid, k)
        else:
            return self.query(2 * node + 1, mid + 1, end, k - self.tree[2 * node])

def solve():
    n = int(input())
    
    counts = [0]
    for _ in range(n - 1):
        counts.append(int(input()))
    
    seg_tree = SegmentTree(n)
    result = []
    
    for i in range(n):
        # 找第counts[i]+1小的編號
        cow_id = seg_tree.query(1, 1, n, counts[i] + 1)
        result.append(cow_id)
        seg_tree.update(1, 1, n, cow_id)
    
    for num in result:
        print(num)

solve()


## 測試用例

*測試輸入與預期輸出*
4
0
1
2

1
2
3
4