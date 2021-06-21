from sys import stdin

n = int(stdin.readline())

for i in range(10, n):
    split_num = sum(list(map(int, str(i))))

    if i + split_num == n:
        print(i)
        break
else:
    print(0)
