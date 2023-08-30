import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)

for i in range(1, n + 1):
    x = int(input())
    graph[x].append(i)

checked = [0] * (n + 1)


def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    print("graph: ", u, graph[u])
    for i in graph[u]:
        if i not in visited:
            dfs(i, visited.copy())
            print("visited: ", visited)
        else:
            result.extend(list(visited))
            print("result: ", result)
            return


result = []
for i in range(1, n + 1):
    if not checked[i]:
        dfs(i, set([]))
