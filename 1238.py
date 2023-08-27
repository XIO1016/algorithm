import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] * n for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

INF = float('inf')


def dijkstra(a):
    q = []
    d = [INF] * (n + 1)
    heapq.heappush(q, (0, a))
    d[a] = 0
    while q:
        dis, cur = heapq.heappop(q)
        if d[cur] >= dis:
            for nxt in graph[cur]:
                cost = dis + nxt[1]
                if cost < d[nxt[0]]:
                    d[nxt[0]] = cost
                    heapq.heappush(q, (cost, nxt[0]))
    return d


ans = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans, go[x] + back[i])

print(ans)
