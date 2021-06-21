from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
select = list(map(int, stdin.readline().split()))
que = deque([i for i in range(1, n + 1)])
count = 0

for i in range(m):
    center = len(que) // 2

    while select[i] != que[0]:
        find = que.index(select[i])

        que.rotate() if find > center else que.rotate(-1)
        count += 1
        
    que.popleft()

print(count)
