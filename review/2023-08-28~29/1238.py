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
    dp = [INF] * (n + 1)
    heapq.heappush(q, (0, a))
    dp[a] = 0
    while q:
        dis, cur = heapq.heappop(q)
        if dp[cur] >= dis:
            for b, c in graph[cur]:
                cost = c + dis
                if cost < dp[b]:
                    dp[b] = cost
                    heapq.heappush(q, (cost, b))
    return dp


ans = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans, go[x] + back[i])
