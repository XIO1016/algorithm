import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(input().strip()) for _ in range(n)]

visited = [[0] * (n + 1) for _ in range(n + 1)]
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
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


cnt1, cnt2 = 0, 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"
visited = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)
