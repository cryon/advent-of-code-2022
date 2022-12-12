from util import lines

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs_distances(graph, start, down=False):
    visited = {start: 0}
    queue = [start]

    while queue:
        current = queue.pop(0)
        for direction in DIRECTIONS:
            neighbour = current[0] + direction[0], current[1] + direction[1]
            if neighbour in visited or neighbour not in graph:
                continue

            if (
                (down and graph[current] - graph[neighbour] <= 1) or
                (not down and graph[neighbour] - graph[current] <= 1)
            ):
                visited[neighbour] = visited[current] + 1
                queue.append(neighbour)
    return visited


def init(path):
    graph, start, end = {}, None, None
    for y, line in enumerate(lines(path, strip=True)):
        for x, c in enumerate(line):
            if c == 'S':
                start = x, y
                graph[x, y] = ord('a')
            elif c == 'E':
                end = x, y
                graph[x, y] = ord('z')
            else:
                graph[x, y] = ord(c)
    return graph, start, end


if __name__ == "__main__":
    graph, start, end = init("input")

    distances_to_top = bfs_distances(graph, start)
    print(f"Distance to top: {distances_to_top[end]}")

    distances_from_top = bfs_distances(graph, end, down=True)
    lowest_points = [k for k, v in graph.items() if v == ord('a')]
    closest_low_point_to_top = min([distances_from_top[c] for c in lowest_points if c in distances_from_top])
    print(f"Shortest distance of any low point to the top: {closest_low_point_to_top}")

