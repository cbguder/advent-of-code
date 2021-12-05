#!/usr/bin/env python3


def main():
    lines = []

    with open('input') as f:
        for line in f:
            pt1, pt2 = line.split(' -> ')
            x1, y1 = map(int, pt1.split(','))
            x2, y2 = map(int, pt2.split(','))
            lines.append(((x1, y1), (x2, y2)))
    
    point_counts = {}
    for line in lines:
        for point in points_on_line(line[0], line[1]):
            point_counts[point] = point_counts.get(point, 0) + 1

    points = 0
    for count in point_counts.values():
        if count > 1:
            points += 1

    print(points)


def points_on_line(start, end):
    x_step = (end[0] > start[0]) - (start[0] > end[0])
    y_step = (end[1] > start[1]) - (start[1] > end[1])

    num_points = abs(end[0] - start[0]) + 1
    if start[0] == end[0]:
        num_points = abs(end[1] - start[1]) + 1

    for i in range(num_points):
        x = start[0] + (x_step * i)
        y = start[1] + (y_step * i)
        yield((x, y))


if __name__ == '__main__':
    main()
