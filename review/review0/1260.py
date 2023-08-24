import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

visited = [0] * (n + 1)
visited1 = [0] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1


def dfs(a):
    visited[a] = 1
    print(a, end=" ")
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[a][i] == 1:
            dfs(i)


def bfs(a):
    q = deque()
    q.append(a)
    visited1[a] = 1
    while q:
        x = q.popleft()
        if visited1[x] == 1:
            print(x, end=" ")
        for i in range(1, n + 1):
            if visited1[i] == 0 and graph[x][i] == 1:
                visited1[i] = 1
                q.append(i)


dfs(v)
print()
bfs(v)
