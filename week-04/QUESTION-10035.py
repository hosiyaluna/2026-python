def solve():
    import sys
    for line in sys.stdin:
        a, b = line.split()
        if a == "0" and b == "0":
            break

        # 反轉字串方便從個位數開始相加
        a = a[::-1]
        b = b[::-1]

        carry = 0
        count = 0
        length = max(len(a), len(b))

        for i in range(length):
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0

            if x + y + carry >= 10:
                count += 1
                carry = 1
            else:
                carry = 0

        if count == 0:
            print("No carry operation.")
        elif count == 1:
            print("1 carry operation.")
        else:
            print(f"{count} carry operations.")
