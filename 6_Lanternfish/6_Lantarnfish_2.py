import sys


def solve(filename):
    f = open(f'{filename}', 'r')
    all_fish = list(map(int, f.read().split(',')))

    for i in range(30):
        to_produce = 0
        print(f'{i}: {len(all_fish)}')
        for i, fish in enumerate(all_fish):
            if fish == 0:
                all_fish[i] = 6
                to_produce += 1
            else:
                all_fish[i] = fish - 1
        for produce in range(to_produce):
            all_fish.append(8)
    return len(all_fish)


if __name__ == "__main__":
    print(solve(sys.argv[1]))
