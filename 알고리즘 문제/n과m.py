from sys import stdin

n, m = map(int, stdin.readline().split())
result = list()

def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n + 1):
        if i not in result:
            result.append(i)
            dfs(i + 1)
            result.pop()

dfs(1)
