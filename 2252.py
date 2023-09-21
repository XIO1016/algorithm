import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]
q = deque()
ans = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
while q:
    tmp = q.popleft()
    ans.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
print(*ans)
