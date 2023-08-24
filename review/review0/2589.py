import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

board = [list(input().strip()) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[0] * n for _ in range(m)]
    visited[a][b] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    cnt = max(cnt, visited[nx][ny])
    return cnt - 1


result = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 'L':
            if i + 1 < m and i - 1 >= 0:
                if board[i + 1][j] == 'L' and board[i - 1][j] == 'L':
                    continue
            if j + 1 < n and j - 1 >= 0:
                if board[i][j + 1] == 'L' and board[i][j - 1] == 'L':
                    continue
            result = max(result, bfs(i, j))
print(result)
