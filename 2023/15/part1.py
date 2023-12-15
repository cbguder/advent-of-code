#!/usr/bin/env python3


def main():
    sum = 0
    with open("input") as f:
        for line in f:
            line = line.strip()
            for p in line.split(","):
                sum += h(p)

    print(sum)


def h(s):
    ret = 0
    for c in s:
        ret = (17 * (ret + ord(c))) % 256
    return ret


if __name__ == "__main__":
    main()
