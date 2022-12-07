from util import lines

FS_SIZE = 70000000
UPDATE_SIZE = 30000000


def solve():
    sizes = dir_sizes("input")

    part1 = sum([s for f, s in sizes.items() if s <= 100000])
    print(f"Part1: {part1}")

    used = sizes[("/",)]
    part2 = sorted([s for s in sizes.values() if (FS_SIZE - used + s >= UPDATE_SIZE)])[0]
    print(f"Part2: {part2}")


def dir_sizes(path):
    sizes = {("/",): 0}
    current_path = []
    for line in lines(path, strip=True):
        match line.split():
            case["$", "cd", ".."]:
                current_path.pop()
            case ["$", "cd", name]:
                current_path.append(name)
            case ["$", _]:
                pass  # ignore other commands for now
            case ["dir", name]:
                sizes[tuple([*current_path, name])] = 0
            case [file_size, _]:
                path = []
                for directory in current_path:
                    path += [directory]
                    sizes[tuple(path)] += int(file_size)
    return sizes


if __name__ == "__main__":
    solve()
