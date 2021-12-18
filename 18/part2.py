#!/usr/bin/env python3


import math
from itertools import permutations


def main():
    pairs = []

    with open('input') as f:
        for line in f:
            pair = parse(line.strip())
            pairs.append(pair)

    max_magnitude = 0
    for pair in permutations(pairs, 2):
        mag = magnitude(reduce(tuple(pair)))
        if mag > max_magnitude:
            max_magnitude = mag

    print(max_magnitude)


def magnitude(item):
    if isinstance(item, int):
        return item

    return 3 * magnitude(item[0]) + 2 * magnitude(item[1])


def reduce(pair):
    while True:
        new_pair = _reduce(pair)
        if new_pair == pair:
            return new_pair

        pair = new_pair


def _reduce(pair):
    new_pair, _, _ = explode(pair)
    if new_pair != pair:
        return new_pair

    new_pair, _ = split(pair)
    return new_pair


def explode(item, level=0):
    if isinstance(item, tuple):
        if level == 4:
            assert isinstance(item[0], int)
            assert isinstance(item[1], int)
            return 0, item[0], item[1]
        else:
            left, cl, cr = explode(item[0], level + 1)
            if cl is not None or cr is not None:
                right, applied = apply_right_carry(item[1], cr)
                if applied:
                    cr = 0
                return (left, right), cl, cr

            right, cl, cr = explode(item[1], level + 1)
            if cl is not None or cr is not None:
                left, applied = apply_left_carry(item[0], cl)
                if applied:
                    cl = 0
                return (left, right), cl, cr

            return (left, right), cl, cr

    return item, None, None


def apply_right_carry(item, carry):
    if carry == 0:
        return item, True

    if isinstance(item, int):
        return item + carry, True

    left, applied = apply_right_carry(item[0], carry)
    if applied:
        right = item[1]
    else:
        right, applied = apply_right_carry(item[1], carry)

    return (left, right), applied


def apply_left_carry(item, carry):
    if carry == 0:
        return item, True

    if isinstance(item, int):
        return item + carry, True

    right, applied = apply_left_carry(item[1], carry)
    if applied:
        left = item[0]
    else:
        left, applied = apply_left_carry(item[0], carry)

    return (left, right), applied


def split(item):
    if isinstance(item, tuple):
        left, done = split(item[0])
        if done:
            right = item[1]
        else:
            right, done = split(item[1])
        return (left, right), done

    assert isinstance(item, int)
    if item >= 10:
        left = math.floor(item / 2)
        right = math.ceil(item / 2)
        return (left, right), True

    return item, False


def parse(line):
    stack = []

    num = None
    for char in line:
        if char.isdigit():
            if num is None:
                num = 0
            num *= 10
            num += int(char)
        elif char in {"]", ","}:
            if num is not None:
                stack.append(num)
            num = None

        if char == "]":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append((num1, num2))

    assert len(stack) == 1
    return stack[0]


if __name__ == '__main__':
    main()
