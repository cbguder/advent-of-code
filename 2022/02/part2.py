#!/usr/bin/env python3


WINS = {"A": "B", "B": "C", "C": "A"}
LOSES = {"B": "A", "C": "B", "A": "C"}
MOVE_SCORES = {"A": 1, "B": 2, "C": 3}


def round_score(opp, me):
    score = MOVE_SCORES[me]

    if me == opp:
        score += 3
    elif WINS[opp] == me:
        score += 6

    return score


def main():
    score = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            opp, outcome = line.split()

            if outcome == "X":
                me = LOSES[opp]
            elif outcome == "Y":
                me = opp
            else:
                me = WINS[opp]

            score += round_score(opp, me)

    print(score)


if __name__ == "__main__":
    main()
