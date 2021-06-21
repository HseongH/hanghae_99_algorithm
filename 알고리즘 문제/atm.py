from sys import stdin

n = int(stdin.readline())
people = sorted(list(map(int, stdin.readline().split())))
result = people[0]

for i in range(1, n):
    people[i] += people[i - 1]
    result += people[i]

print(result)
