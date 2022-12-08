#!/usr/bin/env python3


def scenic_score(grid, x, y):
    tree = grid[x][y]

    height = len(grid)
    width = len(grid[0])

    def score_left():
        score = 0
        for j in range(y-1, -1, -1):
            score += 1
            if grid[x][j] >= tree:
                break
        return score

    def score_right():
        score = 0
        for j in range(y+1, width):
            score += 1
            if grid[x][j] >= tree:
                break
        return score

    def score_top():
        score = 0
        for i in range(x-1, -1, -1):
            score += 1
            if grid[i][y] >= tree:
                break
        return score

    def score_bottom():
        score = 0
        for i in range(x+1, height):
            score += 1
            if grid[i][y] >= tree:
                break
        return score

    return score_top() * score_bottom() * score_left() * score_right()


def main():
    grid = []

    with open("input") as f:
        for line in f:
            line = line.strip()
            row = [int(ch) for ch in line]
            grid.append(row)

    height = len(grid)
    width = len(grid[0])

    max_score = 0

    for i in range(height):
        for j in range(width):
            score = scenic_score(grid, i, j)
            if score > max_score:
                max_score = score

    print(max_score)


if __name__ == "__main__":
    main()
