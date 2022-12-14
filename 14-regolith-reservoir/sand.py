from util import lines, sign


def fall_candidates(s, max_y):
    return [] if s[1] > max_y else [
        (s[0], s[1] + 1),
        (s[0] - 1, s[1] + 1),
        (s[0] + 1, s[1] + 1)
    ]


def drop_sand_grain(cave, spawn, max_y, bottomless=True):
    sand_position = spawn
    while (
        (bottomless and sand_position[1] < max_y) or
        (not bottomless and spawn not in cave)
    ):
        candidates = [c for c in fall_candidates(sand_position, max_y) if c not in cave]
        if not candidates:
            cave.add(sand_position)
            return True
        sand_position = candidates[0]
    return False


def resting_grains_of_sand(cave, max_y, bottomless):
    grains = 0
    while drop_sand_grain(cave, (500, 0), max_y, bottomless):
        grains += 1
    return grains


def construct_cave(path):
    cave, max_y = set(), 0
    for wall_line in read_cave_walls(path):
        max_y = max(max(c[1] for c in wall_line), max_y)
        add_cave_walls(cave, wall_line)
    return cave, max_y


def read_cave_walls(path):
    for line in lines(path, strip=True):
        parts = line.split(" -> ")
        yield list(map(lambda p: (int(p.split(",")[0]), int(p.split(",")[1])), parts))


def add_cave_walls(cave, wall_line):
    for c1, c2 in zip(wall_line, wall_line[1:]):
        d = sign(c2[0] - c1[0]), sign(c2[1] - c1[1])
        current = c1
        while current != c2:
            cave.add(current)
            current = current[0] + d[0], current[1] + d[1]
        cave.add(c2)


if __name__ == "__main__":
    cave, max_y = construct_cave("input")
    part1 = resting_grains_of_sand(cave, max_y, bottomless=True)
    print(f"After {part1} grains of sand the cave starts to overflow")

    cave, max_y = construct_cave("input")
    part2 = resting_grains_of_sand(cave, max_y, bottomless=False)
    print(f"After {part2} grains of sand no more sand can enter the cave")
