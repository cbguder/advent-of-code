#!/usr/bin/env python3


def main():
    count = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            pair = tuple(map(lambda x: tuple(map(int, x.split("-"))), line.split(",")))
            aset = set(range(pair[0][0], pair[0][1] + 1))
            bset = set(range(pair[1][0], pair[1][1] + 1))
            if aset >= bset or bset >= aset:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
