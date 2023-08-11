import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                    cnt += 1
                    board[nx][ny] = 0
                    q.append((nx, ny))
    return cnt


ans = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
print("\n".join(map(str, ans)))
