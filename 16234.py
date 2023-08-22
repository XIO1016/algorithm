import math
import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    union = [(a, b)]
    cnt = graph[a][b]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    union.append((nx, ny))
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += graph[nx][ny]
    for x, y in union:
        graph[x][y] = math.floor(cnt / len(union))
    return len(union)


result = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:
        break
    result += 1
print(result)
