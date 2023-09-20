import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    graph[k][k] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if graph[x][y] == int(1e9):
            print(0, end=' ')
        else:
            print(graph[x][y], end=' ')
    print()
