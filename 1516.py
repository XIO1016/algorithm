import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
indegree = [0] * (n + 1)
time = [0] * (n + 1)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))[:-1]
    time[i] = tmp[0]
    for e in tmp[1:]:
        graph[e].append(i)
        indegree[i] += 1
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]
while q:
    x = q.popleft()
    for e in graph[x]:
        indegree[e] -= 1
        dp[e] = max(dp[e], time[e] + dp[x])
        if indegree[e] == 0:
            q.append(e)

print(*dp[1:], sep='\n')
