from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(s):
    q = deque()
    q.append(s)
    visited = [0] * (n + 1)
    visited[s] = 1
    cnt = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == 0:
                visited[nx] = 1
                q.append(nx)
                cnt += 1
    return cnt


cnt = 0
ans = []
for i in range(1, n + 1):
    ans.append(bfs(i))
cnt = max(ans)
for i in range(n):
    if ans[i] == cnt:
        print(i + 1, end=' ')
