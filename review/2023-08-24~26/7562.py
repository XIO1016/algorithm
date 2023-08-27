import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [1, -1, 1, -1, 2, -2, 2, -2]
dy = [2, 2, -2, -2, 1, 1, -1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if x == c and y == d:
            return visited[c][d]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


for _ in range(t):
    l = int(input())

    a, b = map(int, input().split())
    c, d = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    print(bfs(a, b))
