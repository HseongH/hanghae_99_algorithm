from sys import stdin
from collections import defaultdict

def dfs(graph, start_node):
    visited, need_visit = dict(), list([start_node])

    while need_visit:
        key = need_visit.pop()

        if key not in visited:
            visited[key] = 0
            need_visit.extend(graph[key])

    print(len(visited) - 1)

def creat_graph(temp):
    graph = defaultdict(list)

    for item in temp:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])

    return graph

com = int(stdin.readline())
v = int(stdin.readline())

graph = creat_graph([list(map(int, stdin.readline().split())) for _ in range(v)])

dfs(graph, 1)
