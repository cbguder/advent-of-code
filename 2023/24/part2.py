#!/usr/bin/env python3

import z3


def main():
    points = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split(" @ ")
            p, v = (tuple(map(int, p.split(","))) for p in parts)
            points.append((p, v))

    s = z3.Solver()
    x, y, z = z3.Ints("x y z")
    vx, vy, vz = z3.Ints("vx vy vz")

    for i, (p, v) in enumerate(points):
        t = z3.Int(f"t{i}")
        s.add(x + vx * t == p[0] + v[0] * t)
        s.add(y + vy * t == p[1] + v[1] * t)
        s.add(z + vz * t == p[2] + v[2] * t)

    s.check()
    m = s.model()
    ret = sum(x.as_long() for x in [m[x], m[y], m[z]])
    print(ret)


if __name__ == "__main__":
    main()
