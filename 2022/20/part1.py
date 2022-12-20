#!/usr/bin/env python3


def main():
    nums = []

    i = 0
    with open("input") as f:
        for line in f:
            line = line.strip()
            nums.append((i, int(line)))
            i += 1

    n = len(nums)

    for i in range(n):
        old_idx = -1
        for j in range(n):
            if nums[j][0] == i:
                old_idx = j
                break

        orig_idx, num = nums.pop(old_idx)
        new_idx = (old_idx + num) % n
        if new_idx == 0:
            new_idx = n - 1
        elif new_idx == n - 1:
            new_idx = 0

        foo = old_idx + num
        if foo < 0 or foo >= n:
            new_idx += (old_idx + num) // n

        nums.insert(new_idx, (orig_idx, num))

    zero_idx = -1
    for i in range(n):
        if nums[i][1] == 0:
            zero_idx = i
            break

    total = 0
    for i in range(3):
        idx = zero_idx
        idx += 1000 * (i + 1)
        idx %= n
        total += nums[idx][1]

    print(total)


if __name__ == "__main__":
    main()
