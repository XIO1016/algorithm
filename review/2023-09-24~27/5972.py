import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

d = [int(1e9)] * (n + 1)


def dijkstra(s):
    heap = []
    heapq.heappush(heap, (0, s))
    d[s] = 0
    while heap:
        dis, cur = heapq.heappop(heap)
        if dis <= d[cur]:
            for nxt, nxt_dis in graph[cur]:
                cost = nxt_dis + dis
                if cost < d[nxt]:
                    d[nxt] = cost
                    heapq.heappush(heap, (cost, nxt))
    print(d[n])


dijkstra(1)
