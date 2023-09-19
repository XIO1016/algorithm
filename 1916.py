import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

d = [float('inf')] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

s, e = map(int, input().split())


def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    d[x] = 0
    while q:
        dis, cur = heapq.heappop(q)
        if d[cur] < dis:
            continue
        for nx, nd in graph[cur]:
            cost = dis + nd
            if d[nx] > cost:
                d[nx] = cost
                heapq.heappush(q, (cost, nx))


dijkstra(s)
print(d[e])
