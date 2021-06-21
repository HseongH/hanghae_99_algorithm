n = int(input())
count = 0

while n % 5:
    n -= 3
    count += 1

    if 0 < n < 3:
        print(-1)
        exit()

print(count + n // 5)
