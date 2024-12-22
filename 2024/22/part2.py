#!/usr/bin/env python3

import pyperclip


def main():
    with open("input") as f:
        nums = [int(l) for l in f]

    ret = 0

    sellers = len(nums)
    seqs = {}

    for seller, num in enumerate(nums):
        changes = []

        for i in range(2000):
            new_num = step(num)

            change = (new_num % 10) - (num % 10)
            changes.append(change)

            if len(changes) > 4:
                changes.pop(0)

            if len(changes) == 4:
                k = tuple(changes)
                if k not in seqs:
                    seqs[k] = [0] * sellers
                if seqs[k][seller] == 0:
                    seqs[k][seller] = new_num % 10

            num = new_num

    ret = max(sum(vals) for k, vals in seqs.items())

    print(ret)
    pyperclip.copy(ret)


def step(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num


if __name__ == "__main__":
    main()
