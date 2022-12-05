from itertools import takewhile, dropwhile

from util import lines


def run_gcc(a, m, keep_order=False):
    for move in m:
        q, f, t = move[0], move[1], move[2]
        lifted = a[f - 1][-q:] if keep_order else reversed(a[f - 1][-q:])
        a[t - 1].extend(lifted)
        del a[f - 1][-q:]
    return a


def solve():
    input_lines = lines("input")
    a = run_gcc(arrangement(input_lines), moves(input_lines))
    print(f"Top crates: {''.join([c.pop() for c in a])}")

    input_lines = lines("input")
    a = run_gcc(arrangement(input_lines), moves(input_lines), True)
    print(f"Top crates: {''.join([c.pop() for c in a if len(c)])}")


def arrangement(input_lines):
    layers = [line[1::4] for line in takewhile(lambda l: not l.startswith(" 1"), input_lines)]
    return [list(reversed([c for c in layer if c != ' '])) for layer in zip(*layers)]


def moves(input_lines):
    for line in dropwhile(lambda l: l == '\n',  input_lines):
        yield tuple(map(int, line.split(" ")[1::2]))


if __name__ == "__main__":
    solve()
