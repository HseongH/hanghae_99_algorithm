from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    stack = list()
    brackets = stdin.readline()

    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if len(stack) == 0:
                print('NO')
                break
            stack.pop()
    else:
        if len(stack) > 0:
            print('NO')
        else:
            print('YES')
