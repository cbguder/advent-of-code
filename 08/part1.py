#!/usr/bin/env python3

def main():
    count = 0

    with open('input') as f:
        for line in f:
            parts = line.strip().split(' | ')
            digits = parts[1].split()
            for digit in digits:
                if len(digit) in {2, 3, 4, 7}:
                    count += 1

    print(count)


if __name__ == '__main__':
    main()
