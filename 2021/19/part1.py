#!/usr/bin/env python3

import itertools
import re
from collections import defaultdict
from dataclasses import dataclass

PLUS_MINUSES = [
    ("+", "+", "+"),
    ("+", "+", "-"),
    ("+", "-", "+"),
    ("+", "-", "-"),
    ("-", "+", "+"),
    ("-", "+", "-"),
    ("-", "-", "+"),
    ("-", "-", "-"),
]

ROTATIONS = []


@dataclass(frozen=True)
class Vector:
    x: int
    y: int
    z: int

    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def rotate(self, rotation):
        axis = []

        for attr in rotation:
            if attr.startswith("-"):
                axis.append(-1 * self.__getattribute__(attr[1]))
            else:
                axis.append(self.__getattribute__(attr[1]))

        return Vector(*axis)


def main():
    scans = defaultdict(list)

    scanner_id = None
    scanner_id_re = re.compile(r"--- scanner (\d+) ---")

    with open('input') as f:
        for line in f:
            line = line.strip()
            if line.startswith("---"):
                m = scanner_id_re.match(line)
                scanner_id = int(m[1])
            elif line.strip() != "":
                v = Vector(*map(int, line.split(",")))
                scans[scanner_id].append(v)

    for perm in itertools.permutations(["x", "y", "z"], 3):
        for plusminus in PLUS_MINUSES:
            rotation = tuple(''.join(x) for x in zip(plusminus, perm))
            ROTATIONS.append(rotation)

    res = solve(scans)
    print(res)


def solve(scans):
    normalized_scans = [scans[0]]
    del scans[0]

    while scans:
        for nscan in normalized_scans:
            for key, scan in scans.items():
                rotation, dist = find_overlapping_points(nscan, scan)
                if all((rotation, dist)):
                    normalized_scan = [pt.rotate(rotation) - dist for pt in scan]
                    normalized_scans.append(normalized_scan)
                    del scans[key]
                    break

    unique_points = set()
    for scan in normalized_scans:
        unique_points.update(scan)

    return len(unique_points)


def find_overlapping_points(scan1, scan2):
    for rotation in ROTATIONS:
        scan2_rotated = [pt.rotate(rotation) for pt in scan2]
        dist = _find_overlapping_points(scan1, scan2_rotated)
        if dist is not None:
            return rotation, dist
    return None, None


def _find_overlapping_points(scan1, scan2):
    dists = defaultdict(int)

    for pt1 in scan1:
        for pt2 in scan2:
            # assume these are the same point
            dist = pt2 - pt1
            dists[dist] += 1

            if dists[dist] >= 12:
                return dist

    return None


if __name__ == '__main__':
    main()
