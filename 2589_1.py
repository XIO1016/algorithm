import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(input().strip()) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    visited = [[0] * n for _ in range(m)]
    q.append((a, b))
    visited[a][b] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx, ny))
    return cnt - 1


result = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'L':
            if 0 <= i - 1 and i + 1 < m:
                if graph[i - 1][j] == "L" and graph[i + 1][j] == "L":
                    continue
            if 0 <= j - 1 and j + 1 < n:
                if graph[i][j - 1] == "L" and graph[i][j + 1] == "L":
                    continue
            result = max(bfs(i, j), result)
print(result)
