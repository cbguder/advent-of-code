#!/usr/bin/env python3

from collections import defaultdict


def main():
    a, b = [], []

    with open("input") as f:
        for line in f:
            line = line.strip()
            nums = list(map(int, line.split()))
            a.append(nums[0])
            b.append(nums[1])

    counts = defaultdict(int)
    for x in b:
        counts[x] += 1

    ret = 0
    for x in a:
        ret += x * counts[x]
    print(ret)


if __name__ == "__main__":
    main()
