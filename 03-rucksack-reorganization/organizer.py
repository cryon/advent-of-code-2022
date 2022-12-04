def priority(item):
    return ord(item) - 38 if item.isupper() else ord(item) - 96


def misplaced_priority(c1, c2):
    return priority(set(c1).intersection(c2).pop())


def badge_priority(e1, e2, e3):
    return priority(set(e1).intersection(e2).intersection(e3).pop())


def solve():
    part1 = sum([misplaced_priority(*x) for x in split_input("input")])
    print(f"Priorities of misplaced items: {part1}")

    part2 = sum([badge_priority(*x) for x in chunk_input("input")])
    print(f"Priorities of badges: {part2}")


def split_input(path):
    for line in parse_input(path):
        length = len(line) // 2
        yield line[:length], line[length:]


def chunk_input(path):
    lines = parse_input(path)
    while True:
        try:
            yield next(lines), next(lines), next(lines)
        except StopIteration:
            return


def parse_input(path):
    with open(path, "r") as input_file:
        for line in input_file.readlines():
            yield line.strip()


if __name__ == "__main__":
    solve()

