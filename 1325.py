import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(v):
    q = deque([v])
    visited = [0] * (n + 1)
    visited[v] = 1
    cnt = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt


ans = []
for i in range(1, n + 1):
    ans.append(bfs(i))
m = max(ans)

for i in range(n):
    if m == ans[i]:
        print(i + 1, end=' ')
