
def solve():
    elf_calories = sorted([sum(calories) for calories in parse_input("input")], reverse=True)
    print(f"Hungriest elf: {elf_calories[0]}")
    print(f"Three hungriest elves: {sum(elf_calories[0:3])}")


def parse_input(path):
    with open(path, "r") as input_file:
        chunk = []
        for line in input_file.readlines():
            if line != "\n":
                chunk.append(int(line))
            else:
                yield chunk
                chunk = []


if __name__ == "__main__":
    solve()
