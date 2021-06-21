from sys import stdin

n = int(stdin.readline())
stack = list()

for _ in range(n):
    command = stdin.readline().split()
    
    if command[0] == 'push':
        stack.append(command[1])
        continue
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
            continue
        print(stack.pop())
        continue
    elif command[0] == 'size':
        print(len(stack))
        continue
    elif command[0] == 'empty':
        print(int(len(stack) == 0))
        continue
    else:
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])
        continue
