import sys
import numpy as np


def determine_direction(x1, y1, x2, y2):
    if x1 < x2:
        x_dir = 1
    elif x1 > x2:
        x_dir = -1
    if y1 < y2:
        y_dir = 1
    elif y1 > y2:
        y_dir = -1
    return x_dir, y_dir


def solve(filename):
    f = open(f'{filename}', 'r')
    # ['0,9 -> 5,9',  '8,0 -> 0,8']
    coords = list(map(lambda entry: (tuple(map(int, entry[0].split(','))), tuple(map(
        int, entry[2].split(',')))), list(map(lambda y: y.split(' '), f.read().splitlines()))))
    f.close()

    size_x = 0
    size_y = 0
    for coord in coords:
        start = coord[0]
        end = coord[1]
        size_x = max(size_x, start[0], end[0])
        size_y = max(size_y, start[1], end[1])
    grid = np.zeros((size_x+1, size_y+1), dtype=int)
    for coord in coords:
        x1 = coord[0][0]
        y1 = coord[0][1]
        x2 = coord[1][0]
        y2 = coord[1][1]
        if x1 == x2:
            # +1 due to exclusive bound
            y_range = range(min(y1, y2), max(y1, y2)+1)
            for y in y_range:
                grid[x1][y] += 1
        elif y1 == y2:
            # +1 due to exclusive bound
            x_range = range(min(x1, x2), max(x1, x2)+1)
            for x in x_range:
                grid[x][y1] += 1
        else:  # diagonal
            x_dir, y_dir = determine_direction(x1, y1, x2, y2)
            x_range = range(x1, x2+x_dir, x_dir)
            y_range = range(y1, y2+y_dir, y_dir)
            for i in range(len(x_range)):
                grid[x_range[i]][y_range[i]] += 1
    return np.count_nonzero(grid > 1)


if __name__ == "__main__":
    print(solve(sys.argv[1]))
