#!/usr/bin/env python3
from statistics import median

SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

OPENS = ['(', '[', '{', '<']
CLOSES = [')', ']', '}', '>']


def main():
    scores = []

    with open('input') as f:
        for line in f:
            score = parse(line.strip())
            if score is not None:
                scores.append(score)

    print(int(median(scores)))


def parse(line):
    stack = []

    for ch in line:
        if ch in OPENS:
            stack.append(ch)
        else:
            last_open = stack.pop()
            if CLOSES.index(ch) != OPENS.index(last_open):
                return None

    if len(stack) == 0:
        return None

    score = 0
    while len(stack) > 0:
        open = stack.pop()
        close = CLOSES[OPENS.index(open)]
        score = score * 5 + SCORES[close]

    return score


if __name__ == '__main__':
    main()
