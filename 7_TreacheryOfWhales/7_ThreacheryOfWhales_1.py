import sys

import numpy as np


def solve(filename):
    f = open(f'{filename}', 'r')
    all_crabs = list(map(int, f.read().split(',')))
    sweet_spot = np.median(all_crabs)
    total_fuel = 0
    for crab in all_crabs:
        total_fuel += abs(crab - sweet_spot)

    return int(total_fuel)


if __name__ == "__main__":
    print(solve(sys.argv[1]))
