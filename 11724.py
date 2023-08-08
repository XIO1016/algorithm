import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)


def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = 1
        else:
            bfs(i)
            cnt += 1

print(cnt)
