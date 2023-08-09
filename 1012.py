import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0


for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(m + 1)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    cnt = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
