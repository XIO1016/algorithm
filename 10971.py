import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)
visited = [0] * n


def back_tracking(start, now, total, cnt):
    global ans
    if cnt == n:
        if graph[now][start]:
            total += graph[now][start]
            ans = min(ans, total)
        return
    if total > ans:
        return
    for i in range(n):
        if not visited[i] and graph[now][i]:
            visited[i] = 1
            back_tracking(start, i, total + graph[now][i], cnt + 1)
            visited[i] = 0


for i in range(n):
    visited[i] = 1
    back_tracking(i, i, 0, 1)
    visited[i] = 0
print(ans)
