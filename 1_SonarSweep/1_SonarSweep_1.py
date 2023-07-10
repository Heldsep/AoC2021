import sys


def solve(filename):
    # Read input
    f = open(f'{filename}', 'r')
    input = list(map(int, f.read().splitlines()))
    f.close()

    # Solution
    counter = 0
    last = input[0]
    for new in input[1:]:
        if new > last:
            counter += 1
        last = new

    return counter


if __name__ == "__main__":
    print(solve(sys.argv[1]))
