#!/usr/bin/env python3


def main():
    patterns = []

    pattern = []
    with open("input") as f:
        for line in f:
            line = line.strip()
            if line == "":
                patterns.append(pattern)
                pattern = []
            else:
                pattern.append(line)
    patterns.append(pattern)

    ret = sum(solve(p) for p in patterns)
    print(ret)


def solve(pattern):
    ret = solve_vertical(pattern)
    if ret is not None:
        return ret

    return 100 * solve_horizontal(pattern)


def solve_vertical(pattern):
    cols = []
    for i in range(len(pattern[0])):
        col = "".join(row[i] for row in pattern)
        cols.append(col)

    for i in range(1, len(cols)):
        left = cols[:i]
        right = cols[i:]
        if mirrored(left, right):
            return i

    return None


def solve_horizontal(pattern):
    for i in range(1, len(pattern)):
        top = pattern[:i]
        bottom = pattern[i:]
        if mirrored(top, bottom):
            return i

    return None


def mirrored(x, y):
    diffs = 0

    for a, b in zip(reversed(x), y):
        for c1, c2 in zip(a, b):
            if c1 != c2:
                diffs += 1
                if diffs > 1:
                    return False

    return diffs == 1


if __name__ == "__main__":
    main()
