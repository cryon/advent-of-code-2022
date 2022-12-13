
def lines(path, strip=False, skip_empty=False):
    with open(path, "r") as input_file:
        for line in input_file:
            stripped = line.strip() if strip else line
            if skip_empty and not stripped:
                continue
            yield stripped


def characters(path):
    for line in lines(path):
        for character in line:
            yield character


def whole_file(path):
    with open(path, "r") as input_file:
        return input_file.read()
