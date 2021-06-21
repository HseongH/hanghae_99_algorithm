from sys import stdin

n = int(stdin.readline())

def is_available(current_col, candidate):
    current_row = len(candidate)

    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def dfs(N, current_row, candidate, result):
    if N == current_row:
        result.append(candidate[:])
        return

    for current_col in range(N):
        if is_available(current_col, candidate):
            candidate.append(current_col)
            dfs(N, current_row + 1, candidate, result)
            candidate.pop()

def n_queen(N):
    result = list()
    dfs(N, 0, list(), result)
    print(len(result))

n_queen(n)
