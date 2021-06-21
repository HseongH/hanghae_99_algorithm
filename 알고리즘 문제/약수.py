from sys import stdin

n = int(stdin.readline())
divisor = list(map(int, stdin.readline().split()))

print(max(divisor) * min(divisor))
