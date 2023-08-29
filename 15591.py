import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, q = map(int, input().split())
graph = defaultdict(list)

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs(k, v):
    visited = [0] * (n + 1)
    q = deque()
    q.append(v)
    visited[v] = 1
    cnt = 0
    while q:
        v = q.popleft()
        for nxt, usado in graph[v]:
            if not visited[nxt]:
                if usado >= k:
                    q.append(nxt)
                    cnt += 1
                    visited[nxt] = 1
    return cnt


for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(k, v))
