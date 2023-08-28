import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

INF = float('inf')


def dijkstra():
    d = [INF for _ in range(n + 1)]
    d[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        cur_time, cur = heapq.heappop(q)
        if d[cur] < cur_time:
            continue
        for nxt, nxt_time in graph[cur]:
            time = cur_time + (nxt_time - cur_time) % m
            if d[nxt] > time + 1:
                d[nxt] = time + 1
                heapq.heappush(q, [time + 1, nxt])
    return d[n]


print(dijkstra())
