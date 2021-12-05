#!/usr/bin/env python

from itertools import combinations


def main():
    lines = []

    with open('input') as f:
        for line in f:
            pt1, pt2 = line.split(' -> ')
            x1, y1 = map(int, pt1.split(','))
            x2, y2 = map(int, pt2.split(','))
            lines.append(((x1, y1), (x2, y2)))
    
    common_points = set()
    for line1, line2 in combinations(lines, 2):
        common_points |= find_common_points(line1, line2)

    print(len(common_points))


def find_common_points(line1, line2):
    line1_pts = points_on_line(line1[0], line1[1])
    line2_pts = points_on_line(line2[0], line2[1])
    return line1_pts & line2_pts


def points_on_line(start, end):
    min_x = min(start[0], end[0])
    max_x = max(start[0], end[0])

    min_y = min(start[1], end[1])
    max_y = max(start[1], end[1])

    points = set()

    if min_x == max_x:
        for y in range(min_y, max_y+1):
            points.add((min_x, y))
    elif min_y == max_y:
        for x in range(min_x, max_x+1):
            points.add((x, min_y))

    return points

if __name__ == '__main__':
    main()
