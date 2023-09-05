import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == graph[x][y]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


cnt = 0
visited = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

cnt1 = 0
visited = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt1 += 1
            bfs(i, j)
print(cnt, cnt1)
