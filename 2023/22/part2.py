#!/usr/bin/env python3


def main():
    bricks = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            parts = line.split("~")
            pts = [tuple(map(int, p.split(","))) for p in parts]

            p1 = tuple(min(pts[0][i], pts[1][i]) for i in range(3))
            p2 = tuple(max(pts[0][i], pts[1][i]) for i in range(3))

            bricks.append((p1, p2))

    bricks.sort(key=lambda x: x[0][2])

    surfaces = {}
    supports = {}

    for i, b in enumerate(bricks):
        lev, sups = find_surface(b, surfaces)
        supports[i] = sups

        surf = (b[0][:2], b[1][:2])
        h = b[1][2] - b[0][2] + 1

        surfaces[surf] = (lev + h, i)

    ret = 0
    for i in range(len(bricks)):
        ret += damage(i, supports)

    print(ret)


def damage(base, supports):
    destroyed = {base}

    for b, sups in supports.items():
        if len(sups) > 0 and len(sups - destroyed) == 0:
            destroyed.add(b)

    return len(destroyed) - 1


def find_surface(b, surfaces):
    max_lev = 0
    surf = (b[0][:2], b[1][:2])
    supports = set()
    for rect, (lev, idx) in surfaces.items():
        if overlaps(rect, surf):
            if lev > max_lev:
                max_lev = lev
                supports = {idx}
            elif lev == max_lev:
                supports.add(idx)
    return max_lev, supports


def overlaps(r1, r2):
    return not (r1[1][0] < r2[0][0] or r2[1][0] < r1[0][0] or
                r1[1][1] < r2[0][1] or r2[1][1] < r1[0][1])


if __name__ == "__main__":
    main()
