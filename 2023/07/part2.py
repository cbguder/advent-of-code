#!/usr/bin/env python3

from collections import defaultdict
from functools import cmp_to_key

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def main():
    hands = []

    with open("input") as f:
        for line in f:
            parts = line.strip().split()
            hand = parts[0]
            bid = int(parts[1])
            hands.append((hand, bid))

    hands.sort(key=cmp_to_key(cmp))

    ret = 0
    for i in range(len(hands)):
        ret += hands[i][1] * (i + 1)
    print(ret)


def cmp(a, b):
    a_type = hand_type(a[0])
    b_type = hand_type(b[0])

    if a_type < b_type:
        return 1
    elif a_type > b_type:
        return -1

    for i in range(5):
        a_idx = cards.index(a[0][i])
        b_idx = cards.index(b[0][i])
        if a_idx < b_idx:
            return 1
        elif a_idx > b_idx:
            return -1

    return 0


def hand_type(hand):
    jokers = 0
    counts = defaultdict(int)
    for card in hand:
        if card == "J":
            jokers += 1
        else:
            counts[card] += 1

    x = list(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    if x:
        t = x[0]
        x[0] = (t[0], t[1] + jokers)
        counts = dict(x)
    else:
        counts = {"J": jokers}

    if len(counts) == 1:
        return 0  # FIVE_OF_A_KIND
    elif len(counts) == 2:
        if 4 in counts.values():
            return 1  # FOUR_OF_A_KIND
        else:
            return 2  # FULL_HOUSE
    elif len(counts) == 3:
        if 3 in counts.values():
            return 3  # THREE_OF_A_KIND
        else:
            return 4  # TWO_PAIR
    elif len(counts) == 4:
        return 5  # ONE_PAIR

    return 6  # HIGH_CARD


if __name__ == "__main__":
    main()
