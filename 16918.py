import sys
from collections import deque

input = sys.stdin.readline
r, c, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(q, graph):
    while q:
        x, y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'O':
                graph[nx][ny] = '.'


q = deque()


def simulate(t):
    global graph
    if t == 1:
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append((i, j))
    elif t % 2 == 1:
        bfs(q, graph)
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append((i, j))
    else:
        graph = [['O'] * c for _ in range(r)]


for i in range(1, n + 1):
    simulate(i)

for a in graph:
    print(''.join(a))
