import sys
import numpy as np

NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]
WIDTH = 0
HEIGHT = 0
flashed = []
octopusses = []


def energize_neighbours(octo):
    global flashed
    neighbours = []
    result = 1
    for dir in NEIGHBOURS:
        (x, y) = tuple(map(sum, zip(octo, dir)))
        if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT and (x, y) not in flashed:
            neighbours.append((x, y))
    for (x, y) in neighbours:
        if octopusses[x][y] == 9:
            octopusses[x][y] = 0
            flashed.append((x, y))
            result += energize_neighbours((x, y))
        else:
            if (x, y) not in flashed:
                octopusses[x][y] += 1
    return result


def solve(filename):
    global WIDTH, HEIGHT, flashed, octopusses
    f = open(f'{filename}', 'r')
    lines = f.read().splitlines()
    f.close()
    octopusses = np.array([list(map(int, list(line))) for line in lines])
    WIDTH, HEIGHT = octopusses.shape
    result = 0
    for step in range(100):
        flashed = []
        coords = np.where(octopusses == 9)
        octopusses = octopusses + 1
        to_flash = list(zip(coords[0], coords[1]))
        for coord in to_flash:
            octopusses[coord[0]][coord[1]] = 0
            flashed.append(coord)
            result += energize_neighbours(coord)
    return result


if __name__ == "__main__":
    print(solve(sys.argv[1]))
