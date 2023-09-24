import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    graph[k][k] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

bacon = []
for r in graph:
    bacon.append(sum(r))

print(bacon.index(min(bacon)))
