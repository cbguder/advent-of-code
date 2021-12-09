#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


def main():
    points = []

    with open('input') as f:
        for line in f:
            points.append(list(map(int, [x for x in line.strip()])))

    basin_sizes = []

    for i, row in enumerate(points):
        for j, point in enumerate(row):
            if is_low_point(Coordinate(i, j), points):
                basin = find_basin(Coordinate(i, j), points)
                basin_sizes.append(len(basin))

    basin_sizes = list(reversed(sorted(basin_sizes)))
    res = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print(res)


def is_low_point(pt, points):
    for np in find_neighbors(pt, points):
        if points[np.x][np.y] <= points[pt.x][pt.y]:
            return False

    return True


def find_basin(pt, points):
    basin = {pt}

    while True:
        new_points = set()
        for p in basin:
            for np in find_neighbors(p, points):
                if points[np.x][np.y] > points[p.x][p.y] and points[np.x][np.y] != 9:
                    new_points.add(np)
        if new_points <= basin:
            break
        basin.update(new_points)

    return basin


def find_neighbors(pt, points):
    neighbors = set()

    if pt.x > 0:
        neighbors.add(Coordinate(pt.x - 1, pt.y))
    if pt.x < len(points) - 1:
        neighbors.add(Coordinate(pt.x + 1, pt.y))
    if pt.y > 0:
        neighbors.add(Coordinate(pt.x, pt.y - 1))
    if pt.y < len(points[0]) - 1:
        neighbors.add(Coordinate(pt.x, pt.y + 1))

    return neighbors


if __name__ == '__main__':
    main()
