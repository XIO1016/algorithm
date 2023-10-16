from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
in_degree = [0] * (n + 1)
time = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))[:-1]
    time[i] = tmp[0]
    for t in tmp[1:]:
        graph[t].append(i)
        in_degree[i] += 1

q = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
        dp[i] = time[i]
while q:
    x = q.popleft()
    for nx in graph[x]:
        in_degree[nx] -= 1
        dp[nx] = max(dp[x] + time[nx], dp[nx])
        if in_degree[nx] == 0:
            q.append(nx)
print(*dp[1:], sep='\n')
