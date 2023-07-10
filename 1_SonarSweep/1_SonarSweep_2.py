import sys

PRINT = False


def solve(filename):
    # Read input
    f = open(f'{filename}', 'r')
    input = list(map(int, f.read().splitlines()))
    f.close()

    # Solution
    windowSize = 3
    counter = 0
    A = 0
    for i in range(windowSize):
        A += input[i]
    if PRINT:
        print(f'{A} (N/A - no previous sum)')

    for i in range(1, len(input[1:-1])):
        B = 0
        for j in range(windowSize):
            B += input[i+j]
        if B > A:
            counter += 1
            if PRINT:
                print(f'{B} (increased)')
        elif PRINT:
            if B == A:
                print(f'{B} (no change)')
            else:
                print(f'{B} (decreased)')
        A = B

    return counter


if __name__ == "__main__":
    print(solve(sys.argv[1]))
