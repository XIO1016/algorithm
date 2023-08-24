import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = graph[a][b]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] > visited[x][y] + graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] + graph[nx][ny]
                    q.append((nx, ny))


cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[int(1e9)] * n for _ in range(n)]
    bfs(0, 0)
    print(f'Problem {cnt}: {visited[n - 1][n - 1]}')
    cnt += 1
