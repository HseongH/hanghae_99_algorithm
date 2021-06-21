from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    x, y = map(int, stdin.readline().split())
    distance = y - x
    count = 0
    move = 1
    move_distance = 0

    while move_distance < distance:
        count += 1
        move_distance += move

        if not count % 2:
            move += 1

    print(count)
