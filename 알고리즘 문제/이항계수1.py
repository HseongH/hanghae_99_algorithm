from sys import stdin

N, K = map(int, stdin.readline().split())

fibo = [0] * (N + 1)
fibo[1] = 1

for i in range(2, N + 1):
    fibo[i] = fibo[i - 1] * i

print(fibo[N] // (fibo[K] * fibo[N - K])) if K and K != N else print(1)
