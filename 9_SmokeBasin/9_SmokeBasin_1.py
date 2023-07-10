import sys
import numpy as np


def is_lowest(x, row):
    point = row[x]
    if x == 0:
        if point >= row[x+1]:
            return False
    elif x == len(row)-1:
        if point >= row[x-1]:
            return False
    else:
        if point >= row[x-1] or point >= row[x+1]:
            return False
    return True


def solve(filename):
    f = open(f'{filename}', 'r')
    lines = f.read().splitlines()
    f.close()
    points = np.array([list(map(int, list(line))) for line in lines])

    poi = []
    result = 0
    # find horizontal lowest points
    for y, row in enumerate(points):
        for x in range(len(row)):
            if is_lowest(x, row):
                poi.append((x, y))

    transposed = points.T
    lowest_points = []
    for (x, y) in poi:
        if is_lowest(y, transposed[x]):
            result += points[y][x] + 1
            lowest_points.append((x, y))
    return result


if __name__ == "__main__":
    print(solve(sys.argv[1]))
