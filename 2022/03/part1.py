#!/usr/bin/env python3

def line_score(line):
    n = len(line)
    left, right = line[:n//2], line[n//2:]
    common = set(left) & set(right)
    assert len(common) == 1
    ch = common.pop()

    if "a" <= ch <= "z":
        ret = ord(ch) - ord("a") + 1
    else:
        ret = ord(ch) - ord("A") + 27

    return ret


def main():
    score = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            score += line_score(line)

    print(score)


if __name__ == "__main__":
    main()
