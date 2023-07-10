import sys


def solve(filename):
    # Read input
    f = open(f'{filename}', 'r')
    input = list(map(lambda x: (x[0], int(x[-1])),
                 list(f.read().splitlines())))
    f.close()

    # Solution
    aim = 0
    x = 0
    y = 0
    for (dir, val) in input:
        if dir == 'f':  # forward
            x += val
            y += aim * val
        elif dir == 'u':  # up
            aim -= val
        else:  # down
            aim += val
    return x*y


if __name__ == "__main__":
    print(solve(sys.argv[1]))
