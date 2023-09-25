n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

for i in range(1, m):
    graph[0][i] += graph[0][i - 1]

for i in range(1, n):
    lr = graph[i][:]
    rl = graph[i][:]
    for j in range(m):
        if j == 0:
            lr[j] += graph[i - 1][j]
        else:
            lr[j] += max(graph[i - 1][j], lr[j - 1])
    for j in range(m - 1, -1, -1):
        if j == m - 1:
            rl[j] += graph[i - 1][j]
        else:
            rl[j] += max(graph[i - 1][j], rl[j + 1])
    for j in range(m):
        graph[i][j] = max(lr[j], rl[j])
print(graph[n - 1][m - 1])
