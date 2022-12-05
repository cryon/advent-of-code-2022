from util import lines

scores = {
    'A': 1, 'X': 1,  # rock / lose
    'B': 2, 'Y': 2,  # paper / draw
    'C': 3, 'Z': 3,  # scissors / win
}


def score_round_by_taking_given_move(opponent, me):
    o_score, m_score = scores[opponent], scores[me]
    outcome_score = (m_score - o_score + 1) % 3
    return 3 * outcome_score + m_score


def score_round_by_forcing_given_outcome(opponent, outcome):
    o_score, outcome_score = scores[opponent], scores[outcome]
    m_score = (o_score + outcome_score) % 3
    return 3 * outcome_score + m_score - 2


def solve():
    part1 = sum([score_round_by_taking_given_move(*x) for x in parse_input("input")])
    print(f"Score for part 1: {part1}")

    part2 = sum(score_round_by_forcing_given_outcome(*x) for x in parse_input("input"))
    print(f"Score for part 2: {part2}")


def parse_input(path):
    for line in lines(path):
        yield line.strip().split(" ")


if __name__ == "__main__":
    solve()
