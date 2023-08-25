import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

for i in range(r):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        q = deque([(0, i, graph[i].index('J'))])

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            q.append((-1, i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 'IMPOSSIBLE'

while q:
    time, x, y = q.popleft()

    if time > -1 and graph[x][y] != 'F' and (x == 0 or y == 0 or x == r - 1 or y == c - 1):
        ans = time + 1
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#':
            if time > -1 and graph[nx][ny] == '.':
                graph[nx][ny] = '_'
                q.append((time + 1, nx, ny))
            if time == -1 and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                q.append((-1, nx, ny))
print(ans)
