from sys import stdin

n = int(stdin.readline())
positions = [list(map(int, stdin.readline().split())) for _ in range(n)]
positions.sort(key=lambda x: (x[1], x[0]))

for position in positions:
    print(position[0], position[1])
