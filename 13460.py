import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]


def move(x, y, dx, dy):
    cnt = 0
    while graph[x + dx][y + dy] != "#" and graph[x][y] != 'O':
        cnt += 1
        x += dx
        y += dy
    return x, y, cnt


def bfs(a, b, c, d):
    q = deque()
    q.append((a, b, c, d, 1))
    visited[a][b][c][d] = 1
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if graph[nbx][nby] != "O":
                if graph[nrx][nry] == "O":
                    print(depth)
                    exit()
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = 1
                    q.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)


for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            a, b = i, j
        elif graph[i][j] == "B":
            c, d = i, j

bfs(a, b, c, d)
