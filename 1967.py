import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)
n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dfs(x, w):
    for a, b in graph[x]:
        if dis[a] == -1:
            dis[a] = w + b
            dfs(a, w + b)


dis = [-1] * (n + 1)
dis[1] = 0

dfs(1, 0)

start = dis.index(max(dis))
dis = [-1] * (n + 1)
dis[start] = 0
dfs(start, 0)

print(max(dis))
