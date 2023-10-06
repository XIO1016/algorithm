import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
walls = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            walls.append((i, j))
h, w, sr, sc, fr, fc = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check(i, j):
    for r, c in walls:
        if i <= r < i + h and j <= c < j + w:
            return False
    return True


visited = [[0] * m for _ in range(n)]


def bfs():
    q = deque()
    q.append((sr - 1, sc - 1, 0))
    visited[sr - 1][sc - 1] = 1
    while q:
        x, y, cnt = q.popleft()
        if x == fr - 1 and y == fc - 1:
            print(cnt)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nx + h - 1 < n and 0 <= ny + w - 1 < m:
                if visited[nx][ny] == 0:
                    if check(nx, ny):
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt + 1))
    print(-1)
    return


bfs()
