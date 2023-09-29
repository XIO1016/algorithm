from collections import defaultdict, deque

n = int(input())
k = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 2

direction = defaultdict(int)
for _ in range(int(input())):
    t, d = input().strip().split()
    direction[int(t)] = d

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 1, 1
graph[x][y] = 1
q = deque()
q.append((x, y))
d = 0
time = 0
while True:
    nx, ny = x + dx[d], y + dy[d]
    if 0 >= nx or nx > n or 0 >= ny or ny > n or (nx, ny) in q:
        break
    if graph[nx][ny] != 2:
        a, b = q.popleft()
        graph[a][b] = 1
    x, y = nx, ny
    q.append((x, y))
    time += 1
    if time in direction:
        if direction[time] == "D":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
print(time + 1)
