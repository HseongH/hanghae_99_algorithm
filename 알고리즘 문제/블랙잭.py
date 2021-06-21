from sys import stdin

n, m = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total_score = cards[i] + cards[j] + cards[k]

            if total_score <= m:
                result = max(result, total_score)

print(result)
