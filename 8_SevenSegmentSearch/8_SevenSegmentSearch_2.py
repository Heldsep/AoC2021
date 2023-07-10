import sys

CONSTANTS = [2, 3, 4, 7]


def subtract(s1, s2):
    result = ''
    for s in s1:
        if s not in s2:
            result += s
    return result


def solve(filename):
    f = open(f'{filename}', 'r')
    lines = f.read().splitlines()
    f.close()
    patterns = [sorted([''.join(sorted(entry)) for entry in pattern if entry != ""], key=len)
                for pattern in [line.split('|')[0].split(' ') for line in lines]]
    outputs = [[''.join(sorted(entry)) for entry in pattern if entry != ""]
               for pattern in [line.split('|')[1].split(' ') for line in lines]]

    result = 0

    for index, pattern in enumerate(patterns):
        digits = {}
        digits[1] = pattern[0]
        digits[4] = pattern[2]
        digits[7] = pattern[1]
        digits[8] = pattern[9]

        # number 3
        len_5 = [p for p in pattern if len(p) == 5]
        if len(subtract(len_5[0], len_5[1])) == 2:
            digits[3] = len_5.pop(2)
        else:
            if len(subtract(len_5[0], len_5[2])) == 2:
                digits[3] = len_5.pop(1)
            else:
                digits[3] = len_5.pop(0)

        # number 9
        len_6 = [p for p in pattern if len(p) == 6]
        for i in range(3):
            if len(subtract(len_6[i], digits[3])) == 1:
                digits[9] = len_6.pop(i)
                break

        # number 5 and 2
        b = subtract(digits[9], digits[3])
        if b in len_5[0]:
            digits[5] = len_5[0]
            digits[2] = len_5[1]
        else:
            digits[5] = len_5[1]
            digits[2] = len_5[0]

        # number 0 and 6
        if len(subtract(digits[7], len_6[0])) == 0:
            digits[0] = len_6[0]
            digits[6] = len_6[1]
        else:
            digits[0] = len_6[1]
            digits[6] = len_6[0]
        configs = list(digits.values())
        numbers = list(digits.keys())
        number = ''
        for output in outputs[index]:
            number += str(numbers[configs.index(output)])
        result += int(number)

    return result


if __name__ == "__main__":
    print(solve(sys.argv[1]))
