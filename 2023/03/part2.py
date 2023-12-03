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
                    if char == '*':
                        symbols.append((char, row, col))
                col += 1
            if num != '':
                nums.append((int(num), row, cols))
            row += 1

    sum = 0
    for symbol in symbols:
        adj = list(partno(symbol, nums))
        if len(adj) == 2:
            sum += adj[0] * adj[1]

    print(sum)


def partno(symbol, nums):
    _, srow, scol = symbol
    for val, row, cols in nums:
        if srow - 1 <= row <= srow + 1:
            if min(cols) - 1 <= scol <= max(cols) + 1:
                yield val


if __name__ == "__main__":
    main()
