import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

board = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(m - y1 - 1, m - y2 - 1, -1):
            board[j][i] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = []


def bfs(a, b):
    q = deque()
    q.append((a, b))
    board[a][b] = 1
    s = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    s += 1
                    q.append((nx, ny))
    ans.append(s)


for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            bfs(i, j)

print(len(ans))
ans.sort()
print(*ans)
