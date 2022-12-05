from util import lines


def either_contains(t1, t2):
    return (t1[0] <= t2[0] and t1[1] >= t2[1]) or (
            t2[0] <= t1[0] and t2[1] >= t1[1])


def overlaps(t1, t2):
    return min(t1[1], t2[1]) - max(t1[0], t2[0]) + 1 > 0


def solve():
    part1 = sum([either_contains(x1, x2) for x1, x2 in parse_input("input")])
    print(f"Number of fully overlapping assignments: {part1}")

    part2 = sum([overlaps(x1, x2) for x1, x2 in parse_input("input")])
    print(f"Number of overlapping assignments: {part2}")


def parse_input(path):
    for line in lines(path):
        p1, p2 = line.strip().split(",")
        yield (
            tuple(map(int, p1.split("-"))),
            tuple(map(int, p2.split("-"))))


if __name__ == "__main__":
    solve()
