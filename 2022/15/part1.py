#!/usr/bin/env python3


import re


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    sensors = []
    beacons = set()
    dists = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
            c = list(map(int, m.groups()))
            sensor = tuple(c[:2])
            beacon = tuple(c[2:])
            d = dist(sensor, beacon)

            sensors.append(sensor)
            beacons.add(beacon)
            dists.append(d)

    pts = set()

    for sensor, d0 in zip(sensors, dists):
        for x in range(sensor[0] - d0, sensor[0] + d0 + 1):
            pt = (x, 2000000)
            if pt not in pts and pt not in beacons:
                if dist(pt, sensor) <= d0:
                    pts.add(pt)

    print(len(pts))


if __name__ == "__main__":
    main()
