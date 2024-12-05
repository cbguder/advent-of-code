#!/usr/bin/env python3


def main():
    rules = []
    rules_done = False
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            if line == "":
                rules_done = True
            elif rules_done:
                nums = list(map(int, line.split(",")))
                if in_order(nums, rules):
                    mid = len(nums) // 2
                    ret += nums[mid]
            else:
                parts = tuple(map(int, line.split("|")))
                rules.append(parts)

    print(ret)


def in_order(nums, rules):
    for a, b in rules:
        try:
            i1 = nums.index(a)
            i2 = nums.index(b)
            if i1 > i2:
                return False
        except ValueError:
            continue
    return True


if __name__ == "__main__":
    main()
