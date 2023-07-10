import sys
import numpy as np


def read_bingo_from_txt(filename):
    f = open(f'{filename}', 'r')
    input = f.read().splitlines()
    f.close()

    drawn = [int(x) for x in input[0].split(',')]

    lines = list(filter(''.__ne__, input[1:]))
    blocks = [lines[n:n+5] for n in range(0, len(lines[1:]), 5)]
    boards = [np.array([int(number) for row in block for number in list(
        filter(''.__ne__, row.split(' ')))]) for block in blocks]

    for board in boards:
        board.shape = (5, 5)

    return drawn, np.array(boards)


def solve(filename):
    drawn, boards = read_bingo_from_txt(filename)
    for draw in drawn:
        to_remove = []
        boards[boards == draw] = -1
        if boards.shape[0] == 1:
            if is_done(boards[0]):
                return calculate_result(boards[0], draw)
            else:
                continue
        for i, board in enumerate(boards):
            if is_done(board):
                to_remove.append(i)
        boards = np.delete(boards, to_remove, 0)


def is_done(board):
    trans = board.T
    for i in range(5):
        if all(board[i] == board[i][0]):
            return True
        if all(trans[i] == trans[i][0]):
            return True
    return False


def calculate_result(board, draw):
    sum = board[board >= 0].sum()
    return sum*draw


if __name__ == "__main__":
    print(solve(sys.argv[1]))
