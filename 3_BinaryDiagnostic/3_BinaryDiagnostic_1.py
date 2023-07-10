import sys


def solve(filename):
    # Read input
    f = open(f'{filename}', 'r')
    input = list(f.read().splitlines())
    f.close()

    # process for convience
    processed_input = []  # list with entries being the columns of the input
    for i in range(len(input[0])):
        temp = []
        for entry in input:
            temp.append(entry[i])
        processed_input.append(temp)

    # Solution
    most_occur = []
    least_occur = []
    for col in processed_input:
        x = int(max(col, key=col.count))
        most_occur.append(x)
        least_occur.append(1-x)

    gamma = int(''.join(map(str, most_occur)), 2)
    epsilon = int(''.join(map(str, least_occur)), 2)
    return gamma*epsilon


if __name__ == "__main__":
    print(solve(sys.argv[1]))
