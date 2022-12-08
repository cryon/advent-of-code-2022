from util import lines

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def solve():
    forrest = parse_forrest_grid("input")
    protocol = [inspect_tree(forrest, (x, y)) for x in range(len(forrest[0])) for y in range(len(forrest))]

    print(f"There are {sum([x[0] for x in protocol])} trees visible from the outside")
    print(f"The ideal scenic score is: {sorted([x[1] for x in protocol])[-1]}")


def inspect_tree(forrest, coord):
    visible, scenic_score = False, 1
    for direction in DIRECTIONS:
        v, d = inspect_view_in_direction(forrest, coord, direction)
        visible = visible or v
        scenic_score *= d

    return visible, scenic_score


def inspect_view_in_direction(forrest, coord, direction):
    x, y = coord[0] + direction[0], coord[1] + direction[1]
    visible, view_distance = True, 0

    while visible and 0 <= x < len(forrest[1]) and 0 <= y < len(forrest):
        visible &= forrest[y][x] < forrest[coord[1]][coord[0]]
        view_distance += 1
        x, y = x + direction[0], y + direction[1]

    return visible, view_distance


def parse_forrest_grid(path):
    grid = []
    for line in lines(path, strip=True):
        grid.append(list(map(int, line)))
    return grid


if __name__ == "__main__":
    solve()
