import sys


def solve(filename):
    # Read input
    f = open(f'{filename}', 'r')
    input = list(map(lambda x: (x[0], int(x[-1])),
                 list(f.read().splitlines())))
    f.close()

    # Solution
    x = 0
    y = 0
    for (dir, val) in input:
        if dir == 'f':  # forward
            x += val
        elif dir == 'u':  # up
            y -= val
        else:  # down
            y += val
    return x*y


if __name__ == "__main__":
    print(solve(sys.argv[1]))
