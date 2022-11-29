#!/usr/bin/env python3
import re


def main():
    exp = re.compile(r"(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")

    on_cubes = set()

    with open('input') as f:
        for line in f:
            m = exp.match(line)
            on_off = m[1]
            xmin, xmax = max(-50, int(m[2])), min(50, int(m[3]))
            ymin, ymax = max(-50, int(m[4])), min(50, int(m[5]))
            zmin, zmax = max(-50, int(m[6])), min(50, int(m[7]))

            for x in range(xmin, xmax + 1):
                for y in range(ymin, ymax + 1):
                    for z in range(zmin, zmax + 1):
                        cube = (x, y, z)
                        if on_off == "on":
                            on_cubes.add(cube)
                        elif cube in on_cubes:
                            on_cubes.remove(cube)

    print(len(on_cubes))


if __name__ == '__main__':
    main()
