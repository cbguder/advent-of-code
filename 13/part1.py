#!/usr/bin/env python3

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Fold = namedtuple('Fold', ['axis', 'loc'])


def main():
    points = set()
    folds = []

    with open('input') as f:
        for line in f:
            if line.startswith("fold along"):
                axis, loc = line[11:].strip().split("=")
                folds.append(Fold(axis, int(loc)))
            elif line.strip() != '':
                x, y = tuple(map(int, line.strip().split(",")))
                pt = Point(x, y)
                points.add(pt)

    points = fold(points, folds[0])
    print(len(points))


def fold(points, fold):
    newpoints = set()

    for pt in points:
        if fold.axis == 'x':
            if pt.x > fold.loc:
                newx = 2 * fold.loc - pt.x
                newpoints.add(Point(newx, pt.y))
            else:
                newpoints.add(pt)
        else:
            if pt.y > fold.loc:
                newy = 2 * fold.loc - pt.y
                newpoints.add(Point(pt.x, newy))
            else:
                newpoints.add(pt)

    return newpoints


if __name__ == '__main__':
    main()
