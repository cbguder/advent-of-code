#!/usr/bin/env python3

import re


def main():
    exp = re.compile(r"Player \d starting position: (\d+)")

    pos = []

    with open('input') as f:
        for line in f:
            m = exp.match(line)
            pos.append(int(m[1]))

    score = [0, 0]

    i = 0
    while True:
        roll = i * 9 + 6
        idx = i % 2
        pos[idx] += roll
        while pos[idx] > 10:
            pos[idx] -= 10
        score[idx] += pos[idx]

        i += 1

        if score[idx] >= 1000:
            break

    print(score[i % 2] * i * 3)


if __name__ == '__main__':
    main()
