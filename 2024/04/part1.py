#!/usr/bin/env python3


def main():
    rows = []

    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            rows.append(line)
            ret += xmases(line)

    height = len(rows)
    width = len(rows[0])

    for i in range(width):
        col = "".join([r[i] for r in rows])
        ret += xmases(col)

        diag = diagonal((0, i), rows, 1)
        ret += xmases(diag)

        diag = diagonal((0, i), rows, -1)
        ret += xmases(diag)

    for y in range(1, height):
        diag = diagonal((y, 0), rows, 1)
        ret += xmases(diag)

        diag = diagonal((y, width - 1), rows, -1)
        ret += xmases(diag)

    print(ret)


def xmases(line):
    return line.count("XMAS") + line.count("SAMX")


def diagonal(start, rows, inc_y):
    w = len(rows[0])
    h = len(rows)
    x, y = start
    ret = ""
    while 0 <= x < h and 0 <= y < w:
        ret += rows[x][y]
        x += 1
        y += inc_y
    return ret


if __name__ == "__main__":
    main()
