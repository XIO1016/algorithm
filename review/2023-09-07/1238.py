import heapq
import sys

input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

INF = float("inf")


def dijkstra(a):
    dp = [INF] * (n + 1)
    dp[a] = 0
    q = []
    heapq.heappush(q, (0, a))
    while q:
        dis, cur = heapq.heappop(q)
        if dis <= dp[cur]:
            for nxt, nxt_cost in graph[cur]:
                cost = nxt_cost + dis
                if cost < dp[nxt]:
                    dp[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
    return dp


ans = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans, go[x] + back[i])
print(ans)
