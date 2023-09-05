import copy
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

virus = []
blank_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            blank_cnt += 1
        elif graph[i][j] == 2:
            virus.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

INF = float("inf")


def bfs(q, blanks):
    visited = [[-1] * n for _ in range(n)]
    time = 0
    while True:
        length = len(q)
        if blanks == 0:
            return time
        elif length == 0:
            return INF
        time += 1
        for _ in range(length):
            x, y = q.popleft()
            if visited[x][y] == -1:
                visited[x][y] = 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 0:
                            q.append((nx, ny))
                            visited[nx][ny] = 1
                            blanks -= 1
                        elif graph[nx][ny] == 2:
                            q.append((nx, ny))
                            visited[nx][ny] = 1


ans = INF

for lst in combinations(virus, m):
    q = deque()
    for v in lst:
        q.append(v)
    tmp = bfs(q, blank_cnt)
    ans = min(ans, tmp)

if ans == INF:
    print(-1)
else:
    print(ans)
