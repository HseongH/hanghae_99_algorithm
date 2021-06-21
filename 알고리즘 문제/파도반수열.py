# 처음 생각한 규칙에서 조건에 부합하지 않는 것이 있다면 집요하게 파고들어 보자

from sys import stdin

input = stdin.readline

T = int(input())

sequence = [0] * 101
    
for i in range(1, 4):
    sequence[i] = 1

for i in range(0, 98):
    sequence[i + 3] = sequence[i] + sequence[i + 1]

for _ in range(T):
    n = int(input())

    print(sequence[n])
