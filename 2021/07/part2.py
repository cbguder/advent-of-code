#!/usr/bin/env python3


def main():
    with open('input') as f:
        lines = f.readlines()

    positions = list(map(int, lines[0].split(',')))

    min_pos = min(positions)
    max_pos = max(positions)

    fuel = None
    for dst_pos in range(min_pos, max_pos + 1):
        pos_fuel = fuel_to(dst_pos, positions)
        if fuel is None or pos_fuel < fuel:
            fuel = pos_fuel

    print(fuel)


def fuel_to(dst_pos, positions):
    sum = 0
    for pos in positions:
        dist = abs(dst_pos - pos)
        fuel = (dist * (dist + 1)) / 2
        sum += fuel
    return int(sum)


if __name__ == '__main__':
    main()
