import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
graph = defaultdict(list)

for i in range(N):
    a = int(input())
    graph[a].append(i)

checked = [0] * (N + 1)


def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for i in graph[u]:
        if i not in visited:
            dfs(i, visited.copy())
        else:
            result.extend(list(visited))
            return


result = []
for i in range(1, N + 1):
    if not checked[i]:
        dfs(i, set([]))
result.sort()
print(len(result))
for i in result:
    print(i)
