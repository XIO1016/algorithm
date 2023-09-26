import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [int(input()) for _ in range(n)]


def bfs(a):
    q = deque([a])
    cnt = 0
    for _ in range(n):
        na = q.popleft()
        cnt += 1
        if graph[na] == k:
            return cnt
        q.append(graph[na])
    return -1


print(bfs(0))
