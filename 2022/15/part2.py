#!/usr/bin/env python3


import re


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    sensors = []
    beacons = set()

    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
            c = list(map(int, m.groups()))
            sensor = tuple(c[:2])
            beacon = tuple(c[2:])
            d = dist(sensor, beacon)

            sensors.append((sensor, d))
            beacons.add(beacon)

    for y in range(4000001):
        x = 0

        xranges = [
            sorted([
                sensor[0][0] - sensor[1] + abs(sensor[0][1] - y),
                sensor[0][0] + sensor[1] - abs(sensor[0][1] - y)
            ])
            for sensor in sensors
            if abs(sensor[0][1] - y) <= sensor[1]
        ]

        xranges.sort(key=lambda a: a[0])

        for xrange in xranges:
            min_x = max(0, xrange[0])
            max_x = min(4000000, xrange[1])

            if min_x > x:
                print(4000000 * (x + 1) + y)
                return

            x = max(x, max_x)

        assert x == 4000000


if __name__ == "__main__":
    main()
