import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque([(a, b)])
    visited[a][b] = 1
    seaList = []
    while q:
        sea = 0
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)
    return 1


year = 0
while ice:
    visited = [[0] * m for _ in range(n)]
    arr = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            arr.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(arr)))
    year += 1
if group < 2:
    print(0)
