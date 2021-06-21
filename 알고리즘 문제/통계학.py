from sys import stdin
from collections import Counter

n = int(stdin.readline())
numbers = sorted([int(stdin.readline()) for _ in range(n)])

aver = round(sum(numbers) / n)
center = numbers[n // 2]
cnt = sorted(Counter(numbers).most_common(), key=lambda x: -x[1])
cnt = cnt[0][0] if len(cnt) <= 1 or cnt[1][1] < cnt[0][1] else cnt[1][0]
rng = max(numbers) - min(numbers)

print(aver)
print(center)
print(cnt)
print(rng)
