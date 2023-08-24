import sys
from collections import deque

input = sys.stdin.readline
m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(m - y2, m - y1):
        for j in range(x1, x2):
            graph[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = []


def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                cnt += 1
                graph[nx][ny] = 1
                q.append((nx, ny))
    ans.append(cnt)


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i, j)

ans.sort()
print(len(ans))
print(*ans)
