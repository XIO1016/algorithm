import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)


def dfs(a):
    visited1[a] = 1
    print(a, end=" ")
    for i in range(1, n + 1):
        if visited1[i] == 0 and graph[a][i] == 1:
            dfs(i)


def bfs(a):
    q = deque()
    q.append(a)
    visited2[a] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1, n + 1):
            if visited2[i] == 0 and graph[x][i] == 1:
                visited2[i] = 1
                q.append(i)


dfs(v)
print()
bfs(v)
