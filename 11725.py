import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
ans = [0] * (n + 1)


def bfs():
    q = deque([1])
    visited[1] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                ans[i] = x


bfs()
for i in range(2, n + 1):
    print(ans[i])
