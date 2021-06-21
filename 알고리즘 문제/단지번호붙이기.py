from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
apartment = [list(input().rstrip()) for _ in range(n)]

dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]
result = list()

def bfs(i, j):
    que = deque()
    que.append((i, j))

    apartment[i][j] = '0'
    cnt = 1

    while que:
        pos_y, pos_x = que.popleft()

        for i in range(4):
            y, x = pos_y + dy[i], pos_x + dx[i]

            if 0 <= y < n and 0 <= x < n and apartment[y][x] == '1':
                apartment[y][x] = '0'
                que.append((y, x))
                cnt += 1

    result.append(cnt)

for i in range(n):
    for j in range(n):
        if apartment[i][j] == '1':
            bfs(i, j)

result.sort()

print(len(result))
print('\n'.join(map(str, result)))
