#!/usr/bin/env python3

from functools import cmp_to_key


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
    packets = [
        [[2]],
        [[6]]
    ]

    with open("input") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            packet = parse_packet(line)
            packets.append(packet)

    packets.sort(key=cmp_to_key(cmp_list))
    idx1 = packets.index([[2]]) + 1
    idx2 = packets.index([[6]]) + 1
    print(idx1 * idx2)


if __name__ == "__main__":
    main()
