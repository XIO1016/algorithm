import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] * (n) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

INF = float("inf")


def dijkstra(s):
    d = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, s))
    d[s] = 0
    while q:
        dis, cur = heapq.heappop(q)
        if d[cur] >= dis:
            for nxt, nxt_dis in graph[cur]:
                cost = nxt_dis + dis
                if d[nxt] > cost:
                    d[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
    return d


ans = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans, go[x] + back[i])
