import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

visited = dict()
q = deque()
for i in arr:
    q.append(i)
    visited[i] = 0
while q:
    if k == 0:
        break
    x = q.popleft()
    for nx in [x - 1, x + 1]:
        if nx not in visited and k > 0:
            visited[nx] = visited[x] + 1
            k -= 1
            q.append(nx)
ans = 0
for k, v in visited.items():
    ans += v
print(ans)
