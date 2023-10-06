import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * n
arrive = False


def dfs(a, depth):
    global arrive
    visited[a] = 1
    if depth == 5:
        arrive = True
        return
    for i in graph[a]:
        if visited[i] == 0:
            dfs(i, depth + 1)
    visited[a] = 0


for i in range(n):
    dfs(i, 1)
    if arrive:
        break
print(1 if arrive else 0)
