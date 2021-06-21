from sys import stdin

m, n = map(int, stdin.readline().split())
prime_list = [i for i in range(n + 1)]

for i in range(2, int(n ** 0.5) + 1):
    if prime_list[i]:
        for j in range(2 * i, n + 1, i):
            prime_list[j] = 0

prime_list = list(filter(bool, prime_list[m:]))

for prime in prime_list:
    if prime > 1:
        print(prime)
