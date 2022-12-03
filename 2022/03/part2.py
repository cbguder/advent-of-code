#!/usr/bin/env python3


def line_score(lines):
    sets = list(map(set, lines))
    common = sets[0] & sets[1] & sets[2]
    assert len(common) == 1
    ch = common.pop()

    if "a" <= ch <= "z":
        ret = ord(ch) - ord("a") + 1
    else:
        ret = ord(ch) - ord("A") + 27

    return ret


def main():
    score = 0

    lines = []

    with open("input") as f:
        for line in f:
            lines.append(line.strip())
            if len(lines) == 3:
                score += line_score(lines)
                lines = []

    print(score)


if __name__ == "__main__":
    main()
