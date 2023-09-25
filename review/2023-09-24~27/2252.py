from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = deque()
ans = []
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
while q:
    tmp = q.popleft()
    ans.append(tmp)
    for i in graph[tmp]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)
print(*ans)
