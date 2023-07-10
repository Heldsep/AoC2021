import sys


def solve(filename):
    f = open(f'{filename}', 'r')
    all_fish = list(map(int, f.read().split(',')))
    counters = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }
    for fish in all_fish:
        counters[fish] += 1

    for i in range(256):
        birthgiving = counters[0]
        new_7 = counters[8]
        counters[8] = counters[0]
        for counter in range(6):
            counters[counter] = counters[counter+1]
        counters[6] = birthgiving + counters[7]
        counters[7] = new_7
    return sum(counters.values())


if __name__ == "__main__":
    print(solve(sys.argv[1]))
