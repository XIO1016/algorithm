import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, a, w = map(int, input().split())
    graph[u].append([a, w])
INF = int(1e9)
dp = [INF] * (v + 1)


def dijkstra(s):
    dp[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        dis, cur = heapq.heappop(heap)
        if dis <= dp[cur]:
            for nxt, nxt_cost in graph[cur]:
                cost = nxt_cost + dis
                if cost < dp[nxt]:
                    dp[nxt] = cost
                    heapq.heappush(heap, (cost, nxt))


dijkstra(k)
for i in range(1, v + 1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
