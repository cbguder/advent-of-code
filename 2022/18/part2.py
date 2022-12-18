#!/usr/bin/env python3

from itertools import combinations


def touching(c1, c2):
    return sorted([
        abs(c1[0] - c2[0]),
        abs(c1[1] - c2[1]),
        abs(c1[2] - c2[2]),
    ]) == [0, 0, 1]


def surface(cubes):
    surface = len(cubes) * 6

    for c1, c2 in combinations(cubes, 2):
        if touching(c1, c2):
            surface -= 2

    return surface


def is_in_hole(cube, hole):
    for hole_cube in hole:
        if touching(cube, hole_cube):
            return True
    return False


def add_to_hole(cube, holes):
    matching_holes = set()

    for i, hole in enumerate(holes):
        if is_in_hole(cube, hole):
            matching_holes.add(i)

    if len(matching_holes) == 0:
        holes.append({cube})
    if len(matching_holes) == 1:
        i = matching_holes.pop()
        holes[i].add(cube)
    else:
        merged_hole = {cube}
        for i in sorted(matching_holes, reverse=True):
            merged_hole.update(holes.pop(i))
        holes.append(merged_hole)


def main():
    cubes = set()

    with open("input") as f:
        for line in f:
            line = line.strip()
            cube = tuple(map(int, line.split(",")))
            cubes.add(cube)

    min_x = min(c[0] for c in cubes)
    min_y = min(c[1] for c in cubes)
    min_z = min(c[2] for c in cubes)

    max_x = max(c[0] for c in cubes)
    max_y = max(c[1] for c in cubes)
    max_z = max(c[2] for c in cubes)

    start = (min_x - 1, min_y - 1, min_z - 1)
    fill = {start}
    stack = [start]

    while stack:
        c = stack.pop()
        nexts = {
            (c[0] + 1, c[1], c[2]),
            (c[0] - 1, c[1], c[2]),
            (c[0], c[1] + 1, c[2]),
            (c[0], c[1] - 1, c[2]),
            (c[0], c[1], c[2] + 1),
            (c[0], c[1], c[2] - 1),
        }
        for n in nexts:
            if n in cubes:
                continue

            if n in fill:
                continue

            if not (min_x - 1 <= n[0] <= max_x + 1):
                continue

            if not (min_y - 1 <= n[1] <= max_y + 1):
                continue

            if not (min_z - 1 <= n[2] <= max_z + 1):
                continue

            fill.add(n)
            stack.append(n)

    w = max_x - min_x + 3
    h = max_y - min_y + 3
    d = max_z - min_z + 3

    total_surface = surface(fill)
    total_surface -= 2 * w * h
    total_surface -= 2 * w * d
    total_surface -= 2 * d * h
    print(total_surface)


if __name__ == "__main__":
    main()
