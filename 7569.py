import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

ripe = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                ripe.append((i, j, k))


def bfs():
    while ripe:
        z, x, y = ripe.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1
                    ripe.append((nz, nx, ny))


ans = 0
bfs()
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        ans = max(ans, max(j))

print(ans - 1)
