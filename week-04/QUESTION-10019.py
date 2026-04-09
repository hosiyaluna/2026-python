def solve():
    import sys
    for line in sys.stdin:
        if line.strip() == "":
            continue
        a, b = map(int, line.split())
        print(abs(a - b))