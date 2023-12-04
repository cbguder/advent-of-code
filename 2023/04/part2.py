#!/usr/bin/env python3


def main():
    cards = {}
    idx = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            p1 = line.split(":")
            p2 = p1[1].split("|")
            winning = p2[0].split()
            card = p2[1].split()
            p = pts(card, winning)
            cards[idx] = p
            idx += 1

    stack = list(cards.keys())
    opened = 0
    while stack:
        card = stack.pop()
        opened += 1
        for i in range(card + 1, card + cards[card] + 1):
            stack.append(i)

    print(opened)


def pts(card, winning):
    matching = set(card) & set(winning)
    return len(matching)


if __name__ == "__main__":
    main()
