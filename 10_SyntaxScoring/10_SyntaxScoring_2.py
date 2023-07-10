import sys


def solve(filename):
    f = open(f'{filename}', 'r')
    lines = f.read().splitlines()
    f.close()

    mapping = {'(': ')', '[': ']', '{': '}', '<': '>'}
    closing = [')', ']', '}', '>']
    scoring = {')': 1, ']': 2, '}': 3, '>': 4}

    scores = []

    for line in lines:
        score = 0
        stack = []
        stack.append(line[0])
        for char in line[1:]:
            if char in closing:
                if char == mapping[stack[-1]]:
                    stack.pop()
                else:
                    stack.clear()
                    break
            else:
                stack.append(char)
        if stack:
            for opening in reversed(stack):
                char = mapping[opening]
                score = score*5 + scoring[char]
            scores.append(score)
    return sorted(scores)[int((len(scores)-1)/2)]


if __name__ == "__main__":
    print(solve(sys.argv[1]))
