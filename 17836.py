import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0] * m for _ in range(n)]
sword = 1e9


def bfs():
    global sword
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if graph[x][y] == 2:
            sword = visited[x][y] - 1 + n - 1 - x + m - 1 - y
        if x == n - 1 and y == m - 1:
            return min(sword, visited[x][y] - 1)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return sword


ans = bfs()
print('Fail' if ans > t else ans)
