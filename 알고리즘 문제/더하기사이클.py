n = int(input())
num = n
count = 0

while True:
    temp = num // 10 + num % 10
    num = (num % 10 * 10) + temp % 10
    count += 1

    if num == n:
        break

print(count)
