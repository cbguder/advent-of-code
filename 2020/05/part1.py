#!/usr/bin/env python3

import pyperclip


def seat_id(line):
    row = (0, 127)
    col = (0, 7)

    for c in line:
        if c in {"F", "B"}:
            mid = (row[0] + row[1]) // 2
            if c == "F":
                row = (row[0], mid)
            elif c == "B":
                row = (mid + 1, row[1])
        else:
            mid = (col[0] + col[1]) // 2
            if c == "L":
                col = (col[0], mid)
            elif c == "R":
                col = (mid + 1, col[1])

    return row[0] * 8 + col[0]


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            lid = seat_id(line)
            if lid > ret:
                ret = lid

    print(ret)
    pyperclip.copy(ret)


if __name__ == "__main__":
    main()
