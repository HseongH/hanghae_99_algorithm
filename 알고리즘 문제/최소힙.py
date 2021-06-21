from sys import stdin
import heapq

input = stdin.readline
n = int(input())
heap = list()

for _ in range(n):
    command = int(input())

    if heap and command == 0:
        print(heapq.heappop(heap))
    elif not heap and command == 0:
        print(0)
    else:
        heapq.heappush(heap, command)
