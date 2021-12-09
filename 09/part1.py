#!/usr/bin/env python3

def main():
    points = []

    with open('input') as f:
        for line in f:
            points.append(list(map(int, [x for x in line.strip()])))

    risk = 0

    for i, row in enumerate(points):
        for j, point in enumerate(row):
            if is_low_point(i, j, points):
                risk += point + 1

    print(risk)


def is_low_point(i, j, points):
    neighbors = []

    if i > 0:
        neighbors.append((i - 1, j))
    if i < len(points) - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < len(points[0]) - 1:
        neighbors.append((i, j + 1))

    for x, y in neighbors:
        if points[x][y] <= points[i][j]:
            return False

    return True


if __name__ == '__main__':
    main()
