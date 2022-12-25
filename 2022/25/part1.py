#!/usr/bin/env python3


def decimal_to_snafu(num):
    ret = ""
    while num:
        d = num % 5

        if d < 3:
            ret = str(d) + ret
        elif d == 3:
            ret = "=" + ret
            num += 5
        elif d == 4:
            ret = "-" + ret
            num += 5

        num -= d
        num //= 5

    return ret


def snafu_to_decimal(num):
    ret = 0

    digit = 5 ** (len(num) - 1)
    for d in num:
        if d == "-":
            ret -= digit
        elif d == "=":
            ret -= 2 * digit
        else:
            ret += int(d) * digit

        digit //= 5

    return ret


def main():
    total = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            total += snafu_to_decimal(line)

    print(decimal_to_snafu(total))


if __name__ == "__main__":
    main()
