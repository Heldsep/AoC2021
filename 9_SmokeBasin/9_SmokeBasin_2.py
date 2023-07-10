import sys
import numpy as np

DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
WIDTH = 0
HEIGHT = 0
points = []
seen = []


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


def built_basin(low_coord):
    neighbours = []
    seen.append(low_coord)
    (lowx, lowy) = low_coord
    low = int(points[lowy][lowx])
    for dir in DIRECTIONS:
        (x, y) = tuple(map(sum, zip(low_coord, dir)))
        if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT and (x, y) not in seen:
            neighbours.append((x, y))
    result = 1
    if not neighbours:
        return result
    for (x, y) in neighbours:
        point = int(points[y][x])
        if point >= low and point < 9 and (x, y) not in seen:
            result += built_basin((x, y))
    return result


def solve(filename):
    global WIDTH, HEIGHT, points
    f = open(f'{filename}', 'r')
    lines = f.read().splitlines()
    f.close()
    points = np.array([list(map(int, list(line))) for line in lines])
    WIDTH = len(points[0])
    HEIGHT = len(points.T[0])
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

    basins = []
    for low in lowest_points:
        basins.append(built_basin(low))

    return np.prod(sorted(basins, reverse=True)[:3])


if __name__ == "__main__":
    print(solve(sys.argv[1]))
