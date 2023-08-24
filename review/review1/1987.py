import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 1


def bfs(a, b):
    global ans
    q = {(a, b, board[a][b])}
    while q:
        x, y, z = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] not in z:
                    q.add((nx, ny, z + board[nx][ny]))
                    ans = max(len(z) + 1, ans)


bfs(0, 0)
print(ans)
