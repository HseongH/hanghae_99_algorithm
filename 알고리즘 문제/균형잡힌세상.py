from sys import stdin

while True:
    string = stdin.readline().rstrip()

    if string == '.': break

    stack = list()

    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if len(stack) <= 0:
                print('no')
                break

            bracket = stack.pop()

            if char == ')' and bracket != '(' or char == ']' and bracket != '[':
                print('no')
                break
    else:
        print('no') if stack else print('yes')
