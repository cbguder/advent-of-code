#!/usr/bin/env python3


def is_visible(grid, x, y):
    tree = grid[x][y]

    height = len(grid)
    width = len(grid[0])

    def visible_left():
        for i in range(x):
            if grid[i][y] >= tree:
                return False
        return True

    def visible_right():
        for i in range(height - 1, x, -1):
            if grid[i][y] >= tree:
                return False
        return True

    def visible_top():
        for j in range(y):
            if grid[x][j] >= tree:
                return False
        return True

    def visible_bottom():
        for j in range(width - 1, y, -1):
            if grid[x][j] >= tree:
                return False
        return True

    return visible_top() or visible_bottom() or visible_left() or visible_right()


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            row = [int(ch) for ch in line]
            grid.append(row)

    height = len(grid)
    width = len(grid[0])

    visible = set()

    for i in range(height):
        for j in range(width):
            if is_visible(grid, i, j):
                visible.add((i, j))

    print(len(visible))


if __name__ == "__main__":
    main()
