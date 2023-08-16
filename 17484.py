import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
mx = 100 * n + 1
d = [[[mx] * 3 for _ in range(m)] for _ in range(n)]
for i in range(n):
    if i == 0:
        for j in range(m):
            for k in range(3):
                d[i][j][k] = graph[i][j]
    else:
        for j in range(m):
            if j == 0:
                d[i][j][0] = min(d[i - 1][j + 1][1], d[i - 1][j + 1][2]) + graph[i][j]
                d[i][j][1] = d[i - 1][j][0] + graph[i][j]
            elif j == m - 1:
                d[i][j][1] = d[i - 1][j][2] + graph[i][j]
                d[i][j][2] = min(d[i - 1][j - 1][0], d[i - 1][j - 1][1]) + graph[i][j]
            else:
                d[i][j][0] = min(d[i - 1][j + 1][1], d[i - 1][j + 1][2]) + graph[i][j]
                d[i][j][1] = min(d[i - 1][j][0], d[i - 1][j][2]) + graph[i][j]
                d[i][j][2] = min(d[i - 1][j - 1][0], d[i - 1][j - 1][1]) + graph[i][j]
ans = 100 * n + 1
for i in range(m):
    ans = min(min(d[n - 1][i]), ans)

print(ans)
