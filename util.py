
def lines(path, strip=False):
    with open(path, "r") as input_file:
        for line in input_file:
            if strip:
                yield line.strip()
            else:
                yield line


def characters(path):
    for line in lines(path):
        for character in line:
            yield character

