from sys import stdin
from collections import deque, defaultdict

def dfs(graph, start_node):
    visited, need_visit = dict(), list([start_node])

    while need_visit:
        key = need_visit.pop()

        if key not in visited:
            visited[key] = 0
            need_visit.extend(sorted(graph[key], reverse=True))

    print(' '.join(map(str, visited)))

def bfs(graph, start_node):
    visited, need_visit = dict(), deque([start_node])

    while need_visit:
        key = need_visit.popleft()

        if key not in visited:
            visited[key] = 0
            need_visit.extend(sorted(graph[key]))

    print(' '.join(map(str, visited)))

def create_graph(temp):
    graph = defaultdict(list)

    for item in temp:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])

    return graph

v, edge, start = map(int, stdin.readline().split())
graph = create_graph([list(map(int, stdin.readline().split())) for _ in range(edge)])

dfs(graph, start)
bfs(graph, start)
