import sys

t = int(sys.stdin.readline())

for _ in range(t):
    L = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    swaps = 0
    for i in range(L):
        for j in range(i + 1, L):
            if arr[i] > arr[j]:
                swaps += 1

    print(f"Optimal train swapping takes {swaps} swaps.")