from sys import stdin

n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

start, end = 0, max(trees)
result = list()

while start <= end:
    height = (start + end) // 2
    cut = sum(tree - height for tree in trees if tree > height)

    if m == cut:
        result.append(height)
        break
    elif m < cut:
        result.append(height)
        start = height + 1
    else:
        end = height - 1

print(max(result))
