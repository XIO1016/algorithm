import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = []


def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif board[nx][ny] == 1:
                    visited[nx][ny] = 1
                    board[nx][ny] = 0
                    cnt += 1
    ans.append(cnt)
    return cnt


time = 0
while True:
    time += 1
    visited = [[0] * n for _ in range(m)]
    cnt = bfs(0, 0)
    if cnt == 0:
        break

print(time - 1)
print(ans[-2])
