from sys import stdin

n, k = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(n)]
coins = list(filter(lambda x: x <= k, coins))
count = 0

while k:
    coin = coins.pop()

    if coin <= k:
        count += k // coin
        k %= coin

print(count)
