import sys


def transpose_input(input):
    processed_input = []
    for i in range(len(input[0])):
        temp = []
        for entry in input:
            temp.append(entry[i])
        processed_input.append(temp)
    return processed_input


def determine_most_common(col):
    copy = col.copy()
    copy.sort(reverse=True)  # to ensure 1 in case of equal
    return int(max(copy, key=copy.count))  # most common


def work_out(list, processed_input, oxygen):
    for col_index in range(1, len(processed_input)):
        current_col = transpose_input(list)[col_index]
        x = determine_most_common(current_col)
        if not oxygen:
            x = 1 - x
        new_list = []
        for i, val in enumerate(current_col):
            if int(val) == x:
                new_list.append(list[i])
        if len(new_list) == 1:
            return new_list[0]
        list = new_list


def solve(filename):
    # Read input
    f = open(f'{filename}', 'r')
    input = list(f.read().splitlines())
    f.close()

    # process for convience
    # list with entries being the columns of the input
    processed_input = transpose_input(input)

    # Solution
    oxygen = []
    CO2 = []
    first_col = processed_input[0]
    x = determine_most_common(first_col)
    for i, val in enumerate(first_col):
        if int(val) == x:
            oxygen.append(input[i])
        else:
            CO2.append(input[i])

    x = work_out(oxygen, processed_input, True)
    y = work_out(CO2, processed_input, False)

    oxygen = int(''.join(map(str, x)), 2)
    CO2 = int(''.join(map(str, y)), 2)
    return oxygen * CO2


if __name__ == "__main__":
    print(solve(sys.argv[1]))
