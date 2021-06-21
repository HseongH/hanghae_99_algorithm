from sys import stdin

input = stdin.readline

test_case = int(input())

def number_of_operations(distance):
    square_root = distance ** 0.5

    if round(square_root) >= square_root:
        return round(distance ** 0.5) * 2 - 1
    return round(distance ** 0.5) * 2

for _ in range(test_case):
    x, y = map(int, input().split())
    distance = y - x
    count = number_of_operations(distance)

    print(count)
