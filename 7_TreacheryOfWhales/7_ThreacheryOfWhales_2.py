import sys
import math

import numpy as np


def solve(filename):
    f = open(f'{filename}', 'r')
    all_crabs = list(map(int, f.read().split(',')))
    sweet_spot = math.floor(np.mean(all_crabs))
    total_fuel = 0
    for crab in all_crabs:
        total_fuel += sum(range(1, abs(crab - sweet_spot)+1))

    return total_fuel


if __name__ == "__main__":
    print(solve(sys.argv[1]))
