import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
pos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            pos.append(i)
            pos.append(j)

cnt = 0


def bfs(a, b):
    visited = [[0] * n for _ in range(n)]
    q = deque([(a, b)])
    visited[a][b] = 1
    cand = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[a][b] > graph[nx][ny] != 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))
                elif graph[a][b] == graph[nx][ny] or graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


i, j = pos
size = [2, 0]
while True:
    graph[i][j] = size[0]
    cand = deque(bfs(i, j))
    if not cand:
        break
    step, x, y = cand.popleft()
    cnt += step
    size[1] += 1
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    graph[i][j] = 0
    i, j = x, y

print(cnt)
