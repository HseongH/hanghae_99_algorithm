from sys import stdin

N = 123456 * 2 + 1
prime_list = [True] * N

for i in range(2, int(N ** 0.5) + 1):
    if prime_list[i]:
        for j in range(2 * i, N, i):
            prime_list[j] = False

while True:
    n = int(stdin.readline())

    if n == 0:
        break

    print(len(list(filter(bool, prime_list[n + 1:2 * n + 1]))))
