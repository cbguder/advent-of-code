#!/usr/bin/env python3


def main():
    lines = []

    with open('input') as f:
        lines = [line.strip() for line in f]
    
    draws = map(int, lines[0].split(','))

    boards = []

    for i in range(2, len(lines), 6):
        board = []
        for line in lines[i:i+5]:
            board.append(list(map(int, line.split())))
        
        boards.append(board)
    
    draws_so_far = set()

    for draw in draws:
        draws_so_far.add(draw)
        for board in boards:
            if board_wins(board, draws_so_far):
                score = board_score(board, draws_so_far)
                print(score * draw)
                return


def board_wins(board, draws):
    for i in range(5):
        row = board[i]
        column = [board[j][i] for j in range(5)]

        if set(row).issubset(draws):
            return True
        
        if set(column).issubset(draws):
            return True

    return False


def board_score(board, draws):
    score = 0

    for row in board:
        for number in row:
            if number not in draws:
                score += number

    return score


if __name__ == '__main__':
    main()
