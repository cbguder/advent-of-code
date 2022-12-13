#!/usr/bin/env python3


def parse_packet(line):
    stack = []
    term = None

    for char in line:
        if char == "[":
            stack.append([])
        elif char == "]":
            if term is not None:
                stack[-1].append(term)
            term = stack.pop()
        elif char == ",":
            if term is not None:
                stack[-1].append(term)
            term = None
        else:
            dgt = int(char)
            if term is None:
                term = 0
            term = term * 10 + dgt

    return term


def cmp_list(a, b):
    for ai, bi in zip(a, b):
        if isinstance(ai, int) and isinstance(bi, int):
            if ai > bi:
                return 1
            elif ai < bi:
                return -1
        else:
            if isinstance(ai, int):
                ai = [ai]
            if isinstance(bi, int):
                bi = [bi]
            res = cmp_list(ai, bi)
            if res != 0:
                return res

    if len(a) == len(b):
        return 0
    elif len(b) < len(a):
        return 1

    return -1


def main():
    pairs = []

    with open("input") as f:
        pair = []

        for line in f:
            line = line.strip()
            if line == "":
                continue
            packet = parse_packet(line)
            pair.append(packet)
            if len(pair) == 2:
                pairs.append(pair)
                pair = []

    total = 0
    for i, pair in enumerate(pairs):
        if cmp_list(*pair) == -1:
            total += i + 1

    print(total)


if __name__ == "__main__":
    main()
