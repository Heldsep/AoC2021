import sys


def solve(filename):
    f = open(f'{filename}', 'r')
    lines = f.read().splitlines()
    f.close()

    mapping = {'(': ')', '[': ']', '{': '}', '<': '>'}
    closing = [')', ']', '}', '>']
    scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}

    score = 0

    for line in lines:
        stack = []
        stack.append(line[0])
        for char in line[1:]:
            if char in closing:
                if char == mapping[stack[-1]]:
                    stack.pop()
                else:
                    score += scoring[char]
                    break
            else:
                stack.append(char)
    return score


if __name__ == "__main__":
    print(solve(sys.argv[1]))
