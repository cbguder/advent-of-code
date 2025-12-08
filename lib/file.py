from typing import Optional, TextIO

from lib.grid import Grid
from lib.point import Point, Point3D


class File:
    def __init__(self, f: TextIO) -> None:
        self._f = f

    def read_grid(self) -> Grid[str]:
        rows = [[c for c in line] for line in self.read_lines()]

        return Grid(rows)

    def read_points(self) -> list[Point]:
        return [Point(*map(int, pts)) for pts in self.read_multi_lines(",")]

    def read_points_3d(self) -> list[Point3D]:
        return [Point3D(*map(int, pts)) for pts in self.read_multi_lines(",")]

    def read_lines(self) -> list[str]:
        lines = []

        for line in self._f:
            line = line.strip()
            if line == "":
                break
            lines.append(line)

        return lines

    def read_multi_lines(self, sep: Optional[str] = None) -> list[list[str]]:
        lines = []

        for line in self._f:
            line = line.strip()
            if line == "":
                break
            lines.append(line.split(sep))

        return lines

    def read_line(self) -> str:
        return self._f.readline().strip()
