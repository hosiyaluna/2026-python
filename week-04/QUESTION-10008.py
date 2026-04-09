def solve():
    import sys

    n = int(sys.stdin.readline().strip())
    freq = [0] * 26  # A~Z

    for _ in range(n):
        line = sys.stdin.readline()
        for ch in line:
            if ch.isalpha():
                freq[ord(ch.upper()) - ord('A')] += 1

    # 建立 (字母, 次數) 清單，只保留出現過的
    result = []
    for i in range(26):
        if freq[i] > 0:
            result.append((chr(i + ord('A')), freq[i]))

    # 排序：次數大→小；字母小→大
    result.sort(key=lambda x: (-x[1], x[0]))

    # 輸出
    for letter, count in result:
        print(letter, count)