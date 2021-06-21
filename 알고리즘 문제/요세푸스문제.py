from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
people = [i for i in range(1, n + 1)]
result = list()
ptr = 0

while people:
    ptr = (ptr + (k - 1)) % len(people)

    result.append(people[ptr])
    del people[ptr]

print('<%s>' % ', '.join(map(str, result)))
