import sys

input = sys.stdin.readline

n, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dis = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        dis[i] = min(dis[i - 1] + 1, dis[i])
    for x, y, z in arr:
        if x == i and y <= d and dis[x] + z < dis[y]:
            dis[y] = dis[x] + z
