#!/usr/bin/env python3


def main():
    nums = set()

    with open("input") as f:
        for line in f:
            num = int(line.strip())
            nums.add(num)

    for num in nums:
        ret = solve(2020 - num, nums - {num})
        if ret:
            print(num * ret)
            break


def solve(target, nums):
    for num in nums:
        comp = target - num
        if comp in nums:
            return num * comp
    return None


if __name__ == "__main__":
    main()
