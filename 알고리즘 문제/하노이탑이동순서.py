# 하노이 탑 이동풀이

# 1. 이동해야 할 원반이 하나라면 그 원반을 시작점에서 목표 지점으로 옮기면 된다.
# 2. 이동해야 할 원반이 n개라면 마지막 원반을 목표 원반으로 옮기기 위해 그 위에 위치한 원반들을 모두 보조 기둥으로 옮긴다.
    # 즉, n - 1개의 원반을 보조 기둥을 목표로 모두 옮긴다.
# 3. 모두 보조 원반으로 옮겼다면 1을 수행한다.
# 4. 제일 큰 원반을 목표 기둥으로 옮겼다면 그보다 작은 원반들을 모두 목표 위치로 위치시켜야 한다.
    # 즉, n - 1개의 원반을 초기에 보조 기둥으로 사용하던 위치에서 목표 위치로 옮기고 초기 시작 기둥을 보조 기둥으로 사용한다.

from sys import stdin

count = 0
movement = list()

def hanoi(top, start, end, assist):
    global count
    count += 1

    if top > 1:
        hanoi(top - 1, start, assist, end)

    movement.append((start, end))

    if top > 1:
        hanoi(top - 1, assist, end, start)

n = int(stdin.readline())

hanoi(n, 1, 3, 2)
print(count)

for move in movement:
    print(move[0], move[1])
