import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 1
    while q:
        x, y = q.popleft()
        if x == c and y == d:
            return graph[x][y] - 1
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


for _ in range(t):
    l = int(input())
    graph = [[0] * (l + 1) for _ in range(l + 1)]

    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(bfs(a, b))
