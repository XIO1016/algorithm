import sys

input = sys.stdin.readline

n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]
ans = 0


def dfs(x, y, dsum, cnt):
    global ans
    if cnt == 4:
        ans = max(dsum, ans)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, dsum + paper[nx][ny], cnt + 1)
                visited[nx][ny] = 0


def sol(x, y):
    global ans
    for i in range(4):
        tmp = paper[x][y]
        for j in range(3):
            t = (i + j) % 4
            nx, ny = x + dx[t], y + dy[t]
            if not (0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += paper[nx][ny]
        ans = max(ans, tmp)


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = 0
        sol(i, j)

print(ans)
