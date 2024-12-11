#!/usr/bin/env python3


def main():
    with open("input") as f:
        line = f.read().strip()
        stones = [int(s) for s in line.split()]

    for i in range(25):
        stones = blink(stones)

    print(len(stones))


def blink(stones):
    ret = []

    for s in stones:
        ss = str(s)

        if s == 0:
            ret.append(1)
        elif len(ss) % 2 == 0:
            m = len(ss) // 2
            s1, s2 = ss[:m], ss[m:]
            ret.append(int(s1))
            ret.append(int(s2))
        else:
            ret.append(s * 2024)

    return ret


if __name__ == "__main__":
    main()
