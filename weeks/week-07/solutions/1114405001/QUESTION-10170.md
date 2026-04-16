## 解題代碼

```python
def find_group(S, D):
    # 二分查找第一個 end_day >= D 的旅行團
    left, right = 1, 2 * 10**7  # 足夠大的上界
    
    while left < right:
        mid = (left + right) // 2
        # 第 mid 個旅行團的最後一天
        end_day = mid * S + mid * (mid - 1) // 2
        
        if end_day < D:
            left = mid + 1
        else:
            right = mid
    
    return S + left - 1


# 主程序
import sys

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        S, D = map(int, line.split())
        print(find_group(S, D))
except EOFError:
    pass
```

## 測試用例

*測試輸入與預期輸出*
1

4 5
