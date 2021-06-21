from sys import stdin

n = int(stdin.readline())

stack, result = list(), list()
count = 1

for _ in range(n):
    data = int(stdin.readline())

    while count <= data:
        stack.append(count)
        result.append('+')

        count += 1

    if stack[-1] != data:
        print('NO')
        exit()

    stack.pop()
    result.append('-')

print('\n'.join(result))
