#!/usr/bin/env python3


def main():
    total = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            p1 = line.split(":")
            p2 = p1[1].split("|")
            winning = p2[0].split()
            card = p2[1].split()
            total += pts(card, winning)

    print(total)


def pts(card, winning):
    matching = set(card) & set(winning)
    if len(matching) == 0:
        return 0
    return 2 ** (len(matching) - 1)


if __name__ == "__main__":
    main()
