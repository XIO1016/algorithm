import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[0] * m for _ in range(n)]
    visited[a][b] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == "L":
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx, ny))
    return cnt - 1


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            if 0 <= i - 1 and i + 1 < n:
                if graph[i - 1][j] == "L" and graph[i + 1][j] == "L":
                    continue
            if 0 <= j - 1 and j + 1 < n:
                if graph[i][j - 1] == "L" and graph[i][j + 1] == "L":
                    continue
            result = max(result, bfs(i, j))

print(result)
