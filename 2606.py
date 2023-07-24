import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
pair = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def bfs():
    q = deque()
    q.append(1)
    cnt = 0
    visited[1] = 1
    while q:
        x = q.popleft()
        for i in range(1, n + 1):
            if graph[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    print(cnt)


bfs()
