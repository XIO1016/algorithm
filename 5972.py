import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
INF = float("inf")
d = [INF] * (n + 1)


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    d[s] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if d[cur] >= dist:
            for next in arr[cur]:
                cost = dist + next[1]
                if cost < d[next[0]]:
                    d[next[0]] = cost
                    heapq.heappush(q, (cost, next[0]))
    return d[n]


print(dijkstra(1))
