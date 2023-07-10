import sys
import numpy as np


def solve(filename):
    f = open(f'{filename}', 'r')
    # ['0,9 -> 5,9',  '8,0 -> 0,8']
    coords = list(map(lambda entry: (tuple(map(int, entry[0].split(','))), tuple(map(
        int, entry[2].split(',')))), list(map(lambda y: y.split(' '), f.read().splitlines()))))
    f.close()

    # [((0, 9), (5, 9)), ((0, 0), (8, 8)), ...,  ((5, 5), (8, 2))]
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
            y_range = range(min(y1, y2), max(y1, y2)+1)
            for y in y_range:
                grid[x1][y] += 1
        if y1 == y2:
            x_range = range(min(x1, x2), max(x1, x2)+1)
            for x in x_range:
                grid[x][y1] += 1
    # grid.T
    return np.count_nonzero(grid > 1)


if __name__ == "__main__":
    print(solve(sys.argv[1]))
