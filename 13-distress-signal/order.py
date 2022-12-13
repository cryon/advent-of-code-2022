from functools import cmp_to_key

from util import lines


def cmp_packages(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)

    if not isinstance(left, list):
        return cmp_packages([left], right)

    if not isinstance(right, list):
        return cmp_packages(left, [right])

    if not left and not right: return 0
    if not left: return -1
    if not right: return 1

    c = cmp_packages(left[0], right[0])
    return c if c else cmp_packages(left[1:], right[1:])


def packet_pairs(path):
    ps = list(packets(path))
    return zip(ps[::2], ps[1::2])


def packets(path, extras=[]):
    for line in lines(path, strip=True, skip_empty=True):
        yield eval(line)
    for e in extras:
        yield e


if __name__ == "__main__":
    pairs = packet_pairs("input")
    part1 = sum(i for i, p in enumerate(pairs, start=1) if cmp_packages(*p) <= 0)
    print(f"Sum of indices of pairs that are in correct order: {part1}")

    dividers = [[[2]], [[6]]]
    ps = packets("input", extras=dividers)

    part2 = 1
    for i, p in enumerate(sorted(ps, key=cmp_to_key(cmp_packages)), start=1):
        if p in dividers: part2 *= i

    print(f"Decoder key: {part2}")
