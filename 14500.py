import sys

input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * M for _ in range(N)]

max_value = 0


def dfs(i, j, dsum, cnt):
    global max_value
    if cnt == 4:
        max_value = max(max_value, dsum)
        return
    for n in range(4):
        ni = i + move[n][0]
        nj = j + move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, dsum + paper[ni][nj], cnt + 1)
            visited[ni][nj] = 0


def exce(i, j):
    global max_value
    for n in range(4):
        tmp = paper[i][j]
        for k in range(3):
            t = (n + k) % 4
            ni = i + move[t][0]
            nj = j + move[t][1]
            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += paper[ni][nj]
        max_value = max(max_value, tmp)


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = 0
        exce(i, j)

print(max_value)
