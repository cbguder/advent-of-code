#!/usr/bin/env python3


def main():
    grid = []

    with open("input") as f:
        for line in f:
            grid.append([x for x in line.strip()])

    i = 0
    while True:
        i += 1
        num_moves = step(grid)

        if num_moves == 0:
            print(i)
            break


def step(grid):
    num_moves = 0

    moves = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ">":
                dst = j + 1
                if dst >= len(row):
                    dst = 0
                if grid[i][dst] == '.':
                    moves.append(((i, j), (i, dst)))
    num_moves += len(moves)
    perform_moves(grid, moves)

    moves = []
    for i, row in enumerate(grid):
        dst = i + 1
        if dst >= len(grid):
            dst = 0
        for j, cell in enumerate(row):
            if cell == "v":
                if grid[dst][j] == '.':
                    moves.append(((i, j), (dst, j)))
    num_moves += len(moves)
    perform_moves(grid, moves)

    return num_moves


def perform_moves(grid, moves):
    for src, dst in moves:
        assert grid[dst[0]][dst[1]] == '.'
        grid[dst[0]][dst[1]] = grid[src[0]][src[1]]
        grid[src[0]][src[1]] = '.'


if __name__ == "__main__":
    main()
