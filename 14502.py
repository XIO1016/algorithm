import copy
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]


def bfs():
    global result
    for c in combinations(empty, 3):
        temp = copy.deepcopy(graph)
        for x, y in c:
            temp[x][y] = 1
        virus = [(i, j) for i in range(n) for j in range(m) if temp[i][j] == 2]
        while virus:
            x, y = virus.pop()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    virus.append((nx, ny))
        cnt = 0
        for row in temp:
            cnt += row.count(0)
        result = max(cnt, result)


result = 0
bfs()
print(result)
