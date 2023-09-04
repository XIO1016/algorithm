import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

INF = float("inf")
d = [INF] * (n + 1)


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    d[s] = 0
    while q:
        cur_cost, cur = heapq.heappop(q)
        if d[cur] >= cur_cost:
            for nxt in graph[cur]:
                cost = cur_cost + nxt[1]
                if cost < d[nxt[0]]:
                    d[nxt[0]] = cost
                    heapq.heappush(q, (cost, nxt[0]))
    return d[n]
