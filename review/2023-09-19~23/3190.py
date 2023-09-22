import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 2

l = int(input())
dic = dict()
for _ in range(l):
    x, c = input().split()
    dic[int(x)] = c

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = 1, 1
graph[x][y] = 1
d = 0
time = 0

q = deque()
q.append((x, y))
while True:
    nx, ny = x + dx[d], y + dy[d]
    if nx <= 0 or ny <= 0 or nx > n or ny > n or (nx, ny) in q:
        break
    if graph[ny][nx] != 2:
        a, b = q.popleft()
        graph[b][a] = 0
    x, y = nx, ny
    graph[ny][nx] = 1
    q.append((nx, ny))
    time += 1
    if time in dic.keys():
        if dic[time] == 'D':
            d = (d + 1) % 4
        else:
            d = 3 if d == 0 else d - 1
print(time + 1)
