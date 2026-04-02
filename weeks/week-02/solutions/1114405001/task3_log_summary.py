from collections import defaultdict, Counter


def parse_log(line: str) -> tuple[str, str]:
    user, action = line.split()
    return user, action


def summarize_logs(logs: list[tuple[str, str]]):
    user_counts = defaultdict(int)
    action_counts = Counter()

    for user, action in logs:
        user_counts[user] += 1
        action_counts[action] += 1

    # 次數大→小，同數則名字升序
    user_sorted = sorted(
        user_counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    # 空輸入時回傳 "NONE"
    if action_counts:
        top_action, top_count = action_counts.most_common(1)[0]
    else:
        top_action, top_count = "NONE", 0

    return user_sorted, top_action, top_count


def main():
    m = int(input().strip())

    logs = []
    for _ in range(m):
        logs.append(parse_log(input().strip()))

    user_sorted, top_action, top_count = summarize_logs(logs)

    for user, count in user_sorted:
        print(user, count)

    print(f"top_action: {top_action} {top_count}")


if __name__ == "__main__":
    main()
    main()