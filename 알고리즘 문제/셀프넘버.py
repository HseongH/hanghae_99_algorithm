num_list = [i for i in range(10001)]

def d(n):
    numbers = list(map(int, str(n)))
    idx = n + sum(numbers)

    if idx > 10000:
        return

    num_list[idx] = 0
    d(idx)

for num in num_list:
    if num:
        d(num)

for num in num_list:
    if num:
        print(num)
