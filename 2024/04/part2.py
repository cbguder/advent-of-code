#!/usr/bin/env python3


def main():
    rows = []
    with open("input") as f:
        for line in f:
            line = line.strip()
            rows.append(line)

    ret = 0
    for x in range(len(rows)):
        for y in range(len(rows[0])):
            if is_xmas((x, y), rows):
                ret += 1
    print(ret)


def is_xmas(pos, rows):
    x, y = pos

    if x < 1 or y < 1:
        return False

    w = len(rows[0])
    h = len(rows)
    if x > h - 2 or y > w - 2:
        return False

    if rows[x][y] != "A":
        return False

    diag1 = "".join([rows[x - 1][y - 1], rows[x][y], rows[x + 1][y + 1]])
    diag2 = "".join([rows[x - 1][y + 1], rows[x][y], rows[x + 1][y - 1]])
    return diag1 in {"MAS", "SAM"} and diag2 in {"MAS", "SAM"}


if __name__ == "__main__":
    main()
