from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    h, w, n = map(int, stdin.readline().split())
    floor = n % h if n % h else h
    room = n // h + 1 if n % h else n // h

    print(floor * 100 + room)
