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
                out_of_order = False
                nums = list(map(int, line.split(",")))
                while not in_order(nums, rules):
                    out_of_order = True
                    nums = reorder(nums, rules)
                if out_of_order:
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


def reorder(nums, rules):
    for a, b in rules:
        try:
            i1 = nums.index(a)
            i2 = nums.index(b)
            if i1 > i2:
                ret = nums[:]
                ret[i1], ret[i2] = ret[i2], ret[i1]
                return ret
        except ValueError:
            continue
    return nums


if __name__ == "__main__":
    main()
