import sys

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(input().strip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 1


def bfs(a, b):
    global answer
    q = {(a, b, board[a][b])}
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in ans:
                q.add((nx, ny, ans + board[nx][ny]))
                answer = max(answer, len(ans) + 1)


bfs(0, 0)
print(answer)
