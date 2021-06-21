from sys import stdin

def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)

a, b = map(int, stdin.readline().split())
if a < b: a, b = b, a

common_divisor = gcd(a, b)
common_multiple = common_divisor * (a // common_divisor) * (b // common_divisor)

print(common_divisor)
print(common_multiple)
