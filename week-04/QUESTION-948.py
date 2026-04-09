def solve():
    import sys
    data = sys.stdin.read().strip().split()
    idx = 0

    M = int(data[idx]); idx += 1  # number of test cases

    for _ in range(M):


        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1

        possible_heavy = [True] * (N + 1)
        possible_light = [True] * (N + 1)

        for _ in range(K):
            P = int(data[idx]); idx += 1

            left = list(map(int, data[idx:idx+P]))
            idx += P
            right = list(map(int, data[idx:idx+P]))
            idx += P

            result = data[idx]
            idx += 1

            involved = set(left + right)

            if result == "=":
                # 所有參與的都是真幣
                for coin in involved:
                    possible_heavy[coin] = False
                    possible_light[coin] = False

            elif result == "<":
                # 左邊輕 → 左邊可能輕、右邊可能重
                for i in range(1, N+1):
                    if i in left:
                        possible_heavy[i] = False  # 左邊不可能重
                    elif i in right:
                        possible_light[i] = False  # 右邊不可能輕
                    else:
                        # 不在秤上的全部排除
                        possible_heavy[i] = False
                        possible_light[i] = False

            elif result == ">":
                # 左邊重 → 左邊可能重、右邊可能輕
                for i in range(1, N+1):
                    if i in left:
                        possible_light[i] = False  # 左邊不可能輕
                    elif i in right:
                        possible_heavy[i] = False  # 右邊不可能重
                    else:
                        possible_heavy[i] = False
                        possible_light[i] = False

        # 找出唯一可能的假幣
        candidates = []
        for i in range(1, N+1):
            if possible_heavy[i] or possible_light[i]:
                candidates.append(i)

        if len(candidates) == 1:
            print(candidates[0])
        else:
            print(0)

        print() 