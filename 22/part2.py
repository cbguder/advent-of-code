#!/usr/bin/env python3
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Range:
    start: int
    end: int

    def num_points(self):
        return self.end - self.start + 1

    def split(self, other):
        left = Range(
            min(self.start, other.start),
            max(self.start, other.start) - 1
        )

        middle = Range(
            max(self.start, other.start),
            min(self.end, other.end)
        )

        right = Range(
            min(self.end, other.end) + 1,
            max(self.end, other.end)
        )

        return set(r for r in {left, middle, right} if r.num_points() > 0)

    def contains(self, other):
        return (
                (self.start <= other.start <= self.end)
                and
                (self.start <= other.end <= self.end)
        )

    def __lt__(self, other):
        return self.end < other.start

    def __gt__(self, other):
        return other.end < self.start


@dataclass(frozen=True)
class Cube:
    xrange: Range
    yrange: Range
    zrange: Range

    def num_points(self):
        dx = self.xrange.num_points()
        dy = self.yrange.num_points()
        dz = self.zrange.num_points()
        return dx * dy * dz

    def intersects(self, other):
        if self.xrange < other.xrange or other.xrange < self.xrange:
            return False

        if self.yrange < other.yrange or other.yrange < self.yrange:
            return False

        if self.zrange < other.zrange or other.zrange < self.zrange:
            return False

        return True

    def contains(self, other):
        return (
                self.xrange.contains(other.xrange)
                and
                self.yrange.contains(other.yrange)
                and
                self.zrange.contains(other.zrange)
        )

    def add(self, other):
        if self.contains(other):
            return [self], []

        to_add = []
        rest = []

        for cubelet in self._split(other):
            if self.intersects(cubelet):
                to_add.append(cubelet)
            elif other.intersects(cubelet):
                rest.append(cubelet)

        return to_add, rest

    def remove(self, other):
        to_add = []
        rest = []

        for cubelet in self._split(other):
            if self.intersects(cubelet):
                if not other.intersects(cubelet):
                    to_add.append(cubelet)
            elif other.intersects(cubelet):
                rest.append(cubelet)

        return to_add, rest

    def _split(self, other):
        for xrange in self.xrange.split(other.xrange):
            for yrange in self.yrange.split(other.yrange):
                for zrange in self.zrange.split(other.zrange):
                    yield Cube(xrange, yrange, zrange)


def main():
    exp = re.compile(r"(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")

    on_cubes = []

    with open('input') as f:
        for line in f:
            m = exp.match(line)
            is_on = m[1] == "on"

            xrange = Range(int(m[2]), int(m[3]))
            yrange = Range(int(m[4]), int(m[5]))
            zrange = Range(int(m[6]), int(m[7]))

            cube = Cube(xrange, yrange, zrange)
            on_cubes = insert(on_cubes, cube, is_on)

    on_points = sum(c.num_points() for c in on_cubes)
    print(on_points)


def insert(cubes, new, is_on):
    checked = []

    while cubes:
        cube = cubes.pop()

        if not cube.intersects(new):
            checked.append(cube)
        else:
            if is_on:
                to_add, rest = cube.add(new)
            else:
                to_add, rest = cube.remove(new)
            checked += to_add
            return checked + insert_all(cubes, rest, is_on)

    if is_on:
        return checked + [new]

    return checked


def insert_all(cubes, new_cubes, is_on):
    while new_cubes:
        new = new_cubes.pop()
        cubes = insert(cubes, new, is_on)

    return cubes


def should_be_on(cube, instrs):
    ret = False

    for on_off, instr_cube in instrs:
        if instr_cube.contains(cube):
            ret = on_off

    return ret


if __name__ == '__main__':
    main()
