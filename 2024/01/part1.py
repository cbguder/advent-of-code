#!/usr/bin/env python3


def main():
    a, b = [], []

    with open("input") as f:
        for line in f:
            line = line.strip()
            nums = list(map(int, line.split()))
            a.append(nums[0])
            b.append(nums[1])

    a.sort()
    b.sort()

    ret = 0
    for x, y in zip(a, b):
        ret += abs(x - y)
    print(ret)


if __name__ == "__main__":
    main()
