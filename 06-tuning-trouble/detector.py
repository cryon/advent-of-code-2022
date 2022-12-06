from util import characters


def scan(predicate, iterator, num):
    mem = [None] * num
    for i, c in enumerate(iterator):
        mem.pop(0)
        mem.append(c)
        if predicate(num, mem):
            return i + 1


def all_different(num, data):
    s = set(data)
    return None not in s and len(s) == num


def solve():
    part1 = scan(all_different, characters("input"), 4)
    print(f"Part1: Start of message marker found at: {part1}")

    part2 = scan(all_different, characters("input"), 14)
    print(f"Part2: Start of message marker found at: {part2}")


if __name__ == "__main__":
    solve()
