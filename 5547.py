import sys
from collections import deque

input = sys.stdin.readline

w, h = map(int, input().split())

graph = [[0] * (w + 2) for _ in range(h + 2)]
for i in range(1, h + 1):
    graph[i][1:w + 1] = map(int, input().split())

dx = [0, 1, 1, 0, -1, -1]
dy = [[1, 0, -1, -1, 0, -1], [1, 1, 0, -1, 0, 1]]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[0] * (w + 2) for _ in range(h + 2)]
    visited[a][b] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(6):
            nx, ny = x + dx[i], y + dy[x % 2][i]
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif graph[nx][ny] == 1:
                    cnt += 1
    return cnt


print(bfs(0, 0))
