#!/usr/bin/env python3

import statistics


def main():
    with open('input') as f:
        lines = f.readlines()

    positions = list(map(int, lines[0].split(',')))

    med = statistics.median(positions)
    
    fuel = 0
    for pos in positions:
        fuel += int(abs(pos - med))
    
    print(fuel)


if __name__ == '__main__':
    main()
