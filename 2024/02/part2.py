#!/usr/bin/env python3


def main():
    ret = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            nums = list(map(int, line.split()))
            if is_safe(nums):
                ret += 1

    print(ret)


def is_safe(nums):
    safe = is_safe_internal(nums)
    if safe:
        return True

    for i in range(len(nums)):
        new = nums[:i] + nums[i + 1:]
        safe = is_safe_internal(new)
        if safe:
            return True

    return False


def is_safe_internal(nums):
    last = None

    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if diff == 0 or abs(diff) > 3:
            return False

        if last is not None:
            if diff < 0 < last:
                return False

            if diff > 0 > last:
                return False

        last = diff

    return True


if __name__ == "__main__":
    main()
