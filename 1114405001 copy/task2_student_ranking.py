def parse_student(line: str) -> dict:
    name, score, age = line.split()
    return {
        "name": name,
        "score": int(score),
        "age": int(age),
    }


def rank_students(students: list[dict]) -> list[dict]:
    # 1. score 高到低  2. age 小到大  3. name 字母序
    return sorted(
        students,
        key=lambda s: (-s["score"], s["age"], s["name"])
    )


def top_k_students(students: list[dict], k: int) -> list[dict]:
    ranked = rank_students(students)
    return ranked[:k]


def main():
    n, k = map(int, input().split())

    students = []
    for _ in range(n):
        students.append(parse_student(input().strip()))

    for s in top_k_students(students, k):
        print(s["name"], s["score"], s["age"])


if __name__ == "__main__":
    main()
    main()