import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    global graph
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
    return cnt


ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
print("\n".join(map(str, ans)))
