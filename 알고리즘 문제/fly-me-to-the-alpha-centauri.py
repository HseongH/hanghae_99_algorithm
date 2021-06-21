from sys import stdin

def number_of_operations(distance):
    square_root = distance ** 0.5

    if round(square_root) >= square_root:
        return round(square_root) * 2 - 1
    return round(square_root) * 2

input = stdin.readline

test_case = int(input())

for _ in range(test_case):
    x, y = map(int, input().split())
    distance = y - x
    count = number_of_operations(distance)

    print(count)
