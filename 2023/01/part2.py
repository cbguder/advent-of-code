#!/usr/bin/env python3


def main():
    sum = 0

    digits = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    }

    for i in range(10):
        digits[str(i)] = i

    with open("input") as f:
        for line in f:
            line_digits = []

            for i in range(len(line)):
                for s, d in digits.items():
                    if line[i:].startswith(s):
                        line_digits.append(d)

            sum += line_digits[0] * 10 + line_digits[-1]

    print(sum)


if __name__ == "__main__":
    main()
