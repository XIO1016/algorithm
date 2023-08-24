import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))
    return cnt


arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            arr.append(bfs(i, j))

print(len(arr))
print(*arr)
