#!/usr/bin/env python3

import pyperclip


def main():
    with open("input") as f:
        nums = [int(l) for l in f]

    ret = 0

    for num in nums:
        for i in range(2000):
            num = step(num)
        ret += num

    print(ret)
    pyperclip.copy(ret)


def step(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num


if __name__ == "__main__":
    main()
