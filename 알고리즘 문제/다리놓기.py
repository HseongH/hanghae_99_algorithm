from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    N, M = map(int, stdin.readline().split())

    factorial = [0] * (M + 1)
    factorial[1] = 1

    for i in range(2, M + 1):
        factorial[i] = factorial[i - 1] * i

    print(factorial[M] // (factorial[N] * factorial[M - N])) if N and N != M else print(1)
