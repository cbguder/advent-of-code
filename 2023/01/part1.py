#!/usr/bin/env python3


def main():
    sum = 0

    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    with open("input") as f:
        for line in f:
            line_digits = []

            for char in line:
                if char in digits:
                    line_digits.append(int(char))

            sum += line_digits[0] * 10 + line_digits[-1]

    print(sum)


if __name__ == "__main__":
    main()
