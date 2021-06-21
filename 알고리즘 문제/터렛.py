from sys import stdin

input = stdin.readline

test_case = int(input())

for _ in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)
    R = [r1, r2, r]
    m = max(R)
    R.remove(m)

    print(-1 if (r == 0 and r1 == r2) else 1 if (r == r1 + r2 or m == sum(R)) else 0 if (m > sum(R)) else 2)
