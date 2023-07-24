import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


bfs()
