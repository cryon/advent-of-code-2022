from util import lines


def sign(x):
    return (x > 0) - (x < 0)


def move_rope(rope, move, tail_visited):
    direction, n = move
    for _ in range(n):
        rope[0] = rope[0][0] + direction[0], rope[0][1] + direction[1]  # Update head
        for i in range(1, len(rope)):  # Update tail
            dx, dy = rope[i - 1][0] - rope[i][0], rope[i - 1][1] - rope[i][1]
            if abs(dx) > 1 or abs(dy) > 1:
                rope[i] = rope[i][0] + sign(dx), rope[i][1] + sign(dy)
        tail_visited.add(rope[-1])


def moves(path):
    directions = {'U': (0, 1), 'R': (1, 0), 'L': (-1, 0), 'D': (0, -1)}
    for line in lines(path, strip=True):
        s = line.split()
        yield directions[s[0]], int(s[1])


if __name__ == "__main__":
    rope1, visited1 = [(0, 0)] * 2, set()
    rope2, visited2 = [(0, 0)] * 10, set()

    for head_move in moves("input"):
        move_rope(rope1, head_move, visited1)
        move_rope(rope2, head_move, visited2)

    print(f"For a rope with {len(rope1)} knots, the last visits {len(visited1)} positions")
    print(f"For a rope with {len(rope2)} knots, the last visits {len(visited2)} positions")
