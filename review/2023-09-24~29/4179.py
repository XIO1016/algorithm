from collections import deque

r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]
q = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":
            q.append((i, j, 0))
for i in range(r):
    for j in range(c):
        if graph[i][j] == "F":
            q.append((i, j, -1))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    x, y, time = q.popleft()
    if time > -1 and graph[x][y] != "F" and (x == 0 or x == r - 1 or y == 0 or y == c - 1):
        ans = time + 1
        print(ans)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#":
            if time > -1 and graph[nx][ny] == ".":
                graph[nx][ny] = "-"
                q.append((nx, ny, time + 1))
            elif time == -1 and graph[nx][ny] != "F":
                graph[nx][ny] = "F"
                q.append((nx, ny, -1))
