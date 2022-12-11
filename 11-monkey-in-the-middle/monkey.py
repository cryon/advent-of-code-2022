import operator
import re
from dataclasses import dataclass
from functools import reduce
from typing import Callable

from util import whole_file

MONKEY_PATTERN = (
    "Monkey (?P<number>\\d+):.+?"
    "items: (?P<items>[^\\n]+).+?"
    "Operation: (?P<operation>[^\\n]+).+?"
    "Test: (?P<test>[^\\n]+).+?"
    "true: (?P<true>[^\\n]+).+?"
    "false: (?P<false>[^\\n]+)"
)


@dataclass
class Monkey:
    items: [int]
    operation: Callable[[int], int]
    divisible_by: int
    true_case: int
    false_case: int
    inspected: int = 0


def inspect(monkey, monkeys, modulo=0):
    for item in monkey.items:
        new_worry_level = monkey.operation(item) % modulo if modulo else monkey.operation(item) // 3
        throw_to = monkeys[monkey.false_case] if new_worry_level % monkey.divisible_by else monkeys[monkey.true_case]
        throw_to.items.append(new_worry_level)
        monkey.inspected += 1
    monkey.items = []


def parse_operation(operation_string):
    parts = operation_string.split()
    o = operator.mul if parts[-2] == "*" else operator.add
    if parts[-1] == "old":
        return lambda x: o(x, x)
    else:
        return lambda x: o(x, int(parts[-1]))


def read_monkeys(path):
    monkey_input = whole_file(path)
    matches = re.finditer(MONKEY_PATTERN, monkey_input, flags=re.S)
    return [Monkey(
        items=list(map(int, m.group("items").split(","))),
        operation=parse_operation(m.group("operation")),
        divisible_by=int(m.group("test").split()[-1]),
        true_case=int(m.group("true").split()[-1]),
        false_case=int(m.group("false").split()[-1])
    ) for m in matches]


def run_rounds(num, monkeys, modulo=0):
    for _ in range(num):
        for monkey in monkeys:
            inspect(monkey, monkeys, modulo)


def monkey_business(monkeys):
    inspected = sorted([m.inspected for m in monkeys])
    return inspected[-1] * inspected[-2]


def monkey_modulo(monkeys):
    return reduce(operator.mul, [m.divisible_by for m in monkeys], 1)


if __name__ == "__main__":
    monkeys = read_monkeys("input")
    run_rounds(20, monkeys)
    print(f"Level of monkey business for 20 rounds {monkey_business(monkeys)}")

    monkeys = read_monkeys("input")
    run_rounds(10000, monkeys, monkey_modulo(monkeys))
    print(f"Level of monkey business for 10k rounds {monkey_business(monkeys)}")
