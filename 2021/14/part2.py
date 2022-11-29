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
    pair_counts = count_pairs(chain)
    for i in range(40):
        pair_counts = apply(pair_counts, rules)

    char_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        for char in pair:
            if char != ' ':
                char_counts[char] += count

    a = max(char_counts.values())
    b = min(char_counts.values())
    print(int((a - b) / 2))


def apply(counts, rules):
    newcounts = defaultdict(int)

    for pair, count in counts.items():
        if pair in rules:
            newpairs = [
                pair[0] + rules[pair],
                rules[pair] + pair[1]
            ]
            for newpair in newpairs:
                newcounts[newpair] += count
        else:
            newcounts[pair] += count

    return newcounts


def count_pairs(chain):
    counts = defaultdict(int)

    first_pair = ' ' + chain[0]
    last_pair = chain[-1] + ' '

    counts[first_pair] = 1
    counts[last_pair] = 1

    for i in range(len(chain) - 1):
        pair = chain[i:i + 2]
        counts[pair] += 1

    return counts


if __name__ == '__main__':
    main()
