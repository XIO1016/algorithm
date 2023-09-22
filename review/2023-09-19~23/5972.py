import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
d = [int(1e9)] * (n + 1)


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    d[s] = 0
    while q:
        dis, x = heapq.heappop(q)
        if dis <= d[x]:
            for nx, nx_d in graph[x]:
                cost = nx_d + dis
                if cost < d[nx]:
                    d[nx] = cost
                    heapq.heappush(q, (cost, nx))
    return d[n]


print(dijkstra(1))
