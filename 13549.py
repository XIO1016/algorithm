import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100001


def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = 0
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and visited[nx] == -1:
                if nx == x * 2:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)


print(bfs(n))
