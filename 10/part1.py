#!/usr/bin/env python3

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

OPENS = ['(', '[', '{', '<']
CLOSES = [')', ']', '}', '>']


def main():
    score = 0

    with open('input') as f:
        for line in f:
            score += parse(line.strip())

    print(score)


def parse(line):
    stack = []

    for ch in line:
        if ch in OPENS:
            stack.append(ch)
        else:
            last_open = stack.pop()
            if CLOSES.index(ch) != OPENS.index(last_open):
                return SCORES[ch]

    return 0


if __name__ == '__main__':
    main()
