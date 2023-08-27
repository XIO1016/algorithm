import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ripe = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            ripe.append((i, j))


def bfs():
    while ripe:
        x, y = ripe.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    ripe.append((nx, ny))


bfs()
ans = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
    ans = max(ans, max(tomato[i]))
print(ans - 1)
