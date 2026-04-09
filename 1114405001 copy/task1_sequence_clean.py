def parse_input(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def dedupe_keep_order(seq: list[int]) -> list[int]:
    # 不可直接用 set()，會破壞原始順序
    seen = set()
    result = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


def sort_ascending(seq: list[int]) -> list[int]:
    return sorted(seq)


def sort_descending(seq: list[int]) -> list[int]:
    return sorted(seq, reverse=True)


def filter_evens(seq: list[int]) -> list[int]:
    return [x for x in seq if x % 2 == 0]


def format_output(label: str, seq: list[int]) -> str:
    return f"{label}: " + " ".join(str(x) for x in seq)


def main():
    line = input().strip()
    seq = parse_input(line)

    print(format_output("dedupe", dedupe_keep_order(seq)))
    print(format_output("asc", sort_ascending(seq)))
    print(format_output("desc", sort_descending(seq)))
    print(format_output("evens", filter_evens(seq)))


if __name__ == "__main__":
    main()