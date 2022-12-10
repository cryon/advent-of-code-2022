from util import lines


def compile_program(source):
    program = []
    for instruction in lines(source, strip=True):
        match instruction.split():
            case ["addx", v]:
                program += [0, int(v)]
            case ["noop"]:
                program += [0]
    return program


def execute_program(program, screen):
    x = 1
    for cycle, v in enumerate(program, start=1):
        if (cycle - 20) % 40 == 0:
            yield x * cycle
        scan_x = (cycle - 1) % len(screen[0])
        scan_y = (cycle - 1) // len(screen[0])
        if scan_x in (x - 1, x, x + 1):
            screen[scan_y][scan_x] = "#"
        x += v


def print_screen(screen):
    for row in screen:
        print("".join(row))


if __name__ == "__main__":
    screen = [["."] * 40 for _ in range(6)]
    part1 = sum([o for o in execute_program(compile_program("input"), screen)])
    print(f"The sum of signal strength is: {part1}")
    print_screen(screen)
