#!/usr/bin/env python3


digits = set("0123456789")


def main():
    nums = []
    lines = []
    symbols = []

    with open("input") as f:
        row = 0
        for line in f:
            col = 0
            num = ''
            cols = set()
            line = line.strip()
            lines.append(line)
            for char in line.strip():
                if char in digits:
                    num += char
                    cols.add(col)
                else:
                    if num != '':
                        nums.append((int(num), row, cols))
                        num = ''
                        cols = set()
                    if char != '.':
                        symbols.append((char, row, col))
                col += 1
            if num != '':
                nums.append((int(num), row, cols))
            row += 1

    sum = 0
    for num in nums:
        if partno(num, symbols):
            sum += num[0]

    print(sum)


def partno(num, symbols):
    val, row, cols = num
    mincol = min(cols)
    maxcol = max(cols)
    for sym, srow, scol in symbols:
        if srow - 1 <= row <= srow + 1:
            if mincol - 1 <= scol <= maxcol + 1:
                return True
    return False


if __name__ == "__main__":
    main()
