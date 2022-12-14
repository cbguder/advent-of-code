#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List


class Grid:
    def __init__(self, width, height, base_x):
        self._base_x = base_x
        self._grid = []
        self.total_sand = 0

        for x in range(height):
            self._grid.append([" "] * width)

    def add_line(self, line):
        for i in range(len(line) - 1):
            start = line[i]
            end = line[i + 1]
            if start[0] == end[0]:
                a = min(start[1], end[1])
                b = max(start[1], end[1])
                for y in range(a, b + 1):
                    self.set_at((start[0], y), "#")
            elif start[1] == end[1]:
                a = min(start[0], end[0])
                b = max(start[0], end[0])
                for x in range(a, b + 1):
                    self.set_at((x, start[1]), "#")

    def at(self, pt):
        return self._grid[pt[1]][pt[0] - self._base_x]

    def set_at(self, pt, val):
        self._grid[pt[1]][pt[0] - self._base_x] = val

    def add_sand(self):
        pos = (500, 0)
        while True:
            if pos[1] == len(self._grid) - 1:
                return False

            next = (pos[0], pos[1] + 1)
            val = self.at(next)
            if val == " ":
                pos = next
                continue

            next = (pos[0] - 1, pos[1] + 1)
            val = self.at(next)
            if val == " ":
                pos = next
                continue

            next = (pos[0] + 1, pos[1] + 1)
            val = self.at(next)
            if val == " ":
                pos = next
                continue

            self.set_at(pos, "o")
            self.total_sand += 1
            return True


def main():
    lines = []
    xrange = (1000000, 0)
    max_y = 0

    with open("input") as f:
        for line in f:
            line = line.strip()
            points = [tuple(map(int, x.split(","))) for x in line.split(" -> ")]
            lines.append(points)

            xrange = (
                min(xrange[0], min(p[0] for p in points)),
                max(xrange[1], max(p[0] for p in points))
            )
            max_y = max(max_y, max(p[1] for p in points))

    width = xrange[1] - xrange[0] + 1
    base_x = xrange[0]
    height = max_y + 1

    grid = Grid(width, height, base_x)

    for line in lines:
        grid.add_line(line)

    while True:
        res = grid.add_sand()
        if not res:
            break

    print(grid.total_sand)


if __name__ == "__main__":
    main()
