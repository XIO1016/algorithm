import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(d[i][j])
            exit()
        if j + graph[i][j] < n:
            d[i][j + graph[i][j]] += d[i][j]
        if i + graph[i][j] < n:
            d[i + graph[i][j]][j] += d[i][j]
