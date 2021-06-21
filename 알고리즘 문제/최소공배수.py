from sys import stdin

def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)

t = int(stdin.readline())

for _ in range(t):
    x, y = map(int, stdin.readline().split())
    common_divisor = gcd(x, y)

    print(common_divisor * (x // common_divisor) * (y // common_divisor))
