from sys import stdin

n = int(stdin.readline())
stack = list()

for _ in range(n):
    num = int(stdin.readline())
    stack.append(num) if num else stack.pop()

print(sum(stack))
