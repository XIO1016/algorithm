import heapq
import sys

input = sys.stdin.readline

n, d = map(int, input().split())

graph = [[] for _ in range(d + 1)]
for i in range(d):
    graph[i].append([i + 1, 1])

for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    graph[a].append([b, c])

INF = float("inf")
dis = [INF] * (d + 1)


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dis[s] = 0
    while q:
        cur_dis, cur = heapq.heappop(q)
        if dis[cur] >= cur_dis:
            for nxt, nxt_dis in graph[cur]:
                cost = nxt_dis + cur_dis
                if dis[nxt] > cost:
                    dis[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
    return dis[-1]


print(dijkstra(0))
