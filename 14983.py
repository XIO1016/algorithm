import heapq
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = defaultdict(list)
t = [0] + list(map(int, input().split()))

for i in range(r):
    a, b, l = map(int, input().split())
    heapq.heappush(graph[a], (l, b))
    heapq.heappush(graph[b], (l, a))

for i in graph:
    graph[i].sort()


def dijkstra(s):
    dp = [int(1e9) for _ in range(n + 1)]
    dp[s] = 0
    q = deque()
    q.append((s, 0))
    cnt = 0
    while q:
        cur, dis = q.popleft()
        if dis > dp[cur]:
            continue
        for j in range(len(graph[cur])):
            nxt_dis, nxt = graph[cur][j]
            if nxt_dis + dis < dp[nxt]:
                dp[nxt] = nxt_dis + dis
                q.append((nxt, nxt_dis + dis))

    for i in range(1, n + 1):
        if dp[i] <= m:
            cnt += t[i]
    return cnt


ans = 0
for i in range(1, n + 1):
    ans = max(ans, dijkstra(i))
print(ans)
