import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
hd = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
      (1, -2), (2, -1), (2, 1), (1, 2)]


def bfs():
    q = deque([(0, 0, 0)])
    while q:
        x, y, a = q.popleft()
        if x == h - 1 and y == w - 1:
            return visited[x][y][a] - 1
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][a] and graph[nx][ny] == 0:
                q.append((nx, ny, a))
                visited[nx][ny][a] = visited[x][y][a] + 1
        if a < k:
            for i in range(8):
                nx, ny = x + hd[i][0], y + hd[i][1]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny][a + 1] and graph[nx][ny] == 0:
                    q.append((nx, ny, a + 1))
                    visited[nx][ny][a + 1] = visited[x][y][a] + 1

    return -1


visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
visited[0][0][0] = 1
print(bfs())
