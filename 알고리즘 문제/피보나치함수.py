from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    n = int(stdin.readline())

    fibo = [0] * (n + 1)
    if n >= 1: fibo[1] = 1

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibo[-2], fibo[-1])
