#!/usr/bin/env python3

from collections import defaultdict


def main():
    with open('input') as f:
        lines = [l.strip() for l in f.readlines()]

    template = lines[0]

    rules = {}
    for line in lines[2:]:
        k, v = line.split(' -> ')
        rules[k] = v

    chain = template
    for i in range(10):
        chain = apply(chain, rules)

    counts = defaultdict(int)
    for char in chain:
        counts[char] += 1

    a = max(counts.values())
    b = min(counts.values())
    print(a - b)


def apply(chain, rules):
    newchain = chain[0]

    for i in range(len(chain) - 1):
        pair = chain[i:i + 2]
        if pair in rules:
            newchain += rules[pair]
        newchain += pair[1]

    return newchain


if __name__ == '__main__':
    main()
