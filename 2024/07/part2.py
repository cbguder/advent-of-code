#!/usr/bin/env python3


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split(": ")
            val = int(parts[0])
            nums = list(map(int, parts[1].split()))
            if works(val, nums):
                ret += val

    print(ret)


def works(val, nums):
    for v in vals(nums):
        if v == val:
            return True

    return False


def vals(nums):
    if len(nums) == 1:
        yield nums[0]
        return

    for v in vals(nums[:-1]):
        yield v + nums[-1]
        yield v * nums[-1]
        yield int(str(v) + str(nums[-1]))


if __name__ == "__main__":
    main()
