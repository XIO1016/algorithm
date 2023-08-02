import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

pizza = [list(map(int, input().split())) for _ in range(a)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = []


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < a and 0 <= ny < b and visited[nx][ny] == 0:
                if pizza[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif pizza[nx][ny] == 1:
                    visited[nx][ny] = 1
                    pizza[nx][ny] = 0
                    cnt += 1
    ans.append(cnt)
    return cnt


time = 0
while True:
    time += 1
    visited = [[0] * b for _ in range(a)]
    cnt = bfs()
    if cnt == 0:
        break

print(time - 1)
print(ans[-2])
