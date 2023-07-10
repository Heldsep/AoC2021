import sys

CONSTANTS = [2, 3, 4, 7]


def solve(filename):
    f = open(f'{filename}', 'r')
    lines = f.read().splitlines()
    f.close()
    outputs = [[entry for entry in pattern if entry != ""]
               for pattern in [line.split('|')[1].split(' ') for line in lines]]

    total = 0
    for output in outputs:
        for digit in output:
            if len(digit) in CONSTANTS:
                total += 1
    return total


if __name__ == "__main__":
    print(solve(sys.argv[1]))
