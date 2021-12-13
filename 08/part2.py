#!/usr/bin/env python3

from collections import defaultdict

SEGMENTS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def main():
    total = 0

    with open('input') as f:
        for line in f:
            parts = line.strip().split(' | ')
            signals, digits = [p.split() for p in parts]
            total += decode(signals, digits)

    print(total)


def decode(signals, digits):
    signals_by_length = defaultdict(list)
    for signal in signals:
        signals_by_length[len(signal)].append(set(x for x in signal))

    mapping = {}
    mapping['cf'] = signals_by_length[2][0]
    mapping['acf'] = signals_by_length[3][0]
    mapping['bcdf'] = signals_by_length[4][0]
    mapping['abcdefg'] = signals_by_length[7][0]

    mapping['bd'] = mapping['bcdf'] - mapping['cf']

    mapping['a'] = mapping['acf'] - mapping['cf']
    mapping['eg'] = mapping['abcdefg'] - (mapping['bcdf'] | mapping['a'])
    mapping['bcef'] = (signals_by_length[5][0] | signals_by_length[5][1] | signals_by_length[5][2]) - (
            signals_by_length[5][0] & signals_by_length[5][1] & signals_by_length[5][2])
    mapping['abfg'] = (signals_by_length[6][0] & signals_by_length[6][1] & signals_by_length[6][2])
    mapping['d'] = mapping['bcdf'] - mapping['bcef']
    mapping['e'] = mapping['bcef'] - mapping['bcdf']
    mapping['g'] = mapping['eg'] - mapping['e']
    mapping['b'] = mapping['bd'] - mapping['d']
    mapping['c'] = mapping['bd'] - mapping['d']
    mapping['f'] = mapping['abfg'] - (mapping['a'] | mapping['b'] | mapping['g'])
    mapping['c'] = mapping['cf'] - mapping['f']

    reverse_mapping = {}
    for k, v in mapping.items():
        if len(k) == 1:
            assert len(v) == 1
            reverse_mapping[list(v)[0]] = k

    res = 0

    for digit in digits:
        res *= 10
        segments = set()
        for s in digit:
            segments.add(reverse_mapping[s])
        key = "".join(sorted(list(segments)))
        num = SEGMENTS[key]
        res += num

    return res


if __name__ == '__main__':
    main()
