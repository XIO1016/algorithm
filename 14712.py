import sys

input = sys.stdin.readline
n, m = map(int, input().split())

ans = 0
visited = [[0] * (m + 1) for _ in range(n + 1)]


def back_tracking(depth):
    global ans
    if depth == n * m:
        ans += 1
        return
    x = depth // m + 1
    y = depth % m + 1

    back_tracking(depth + 1)
    if visited[x - 1][y] == 0 or visited[x][y - 1] == 0 or visited[x - 1][y - 1] == 0:
        visited[x][y] = 1
        back_tracking(depth + 1)
        visited[x][y] = 0


back_tracking(0)
print(ans)
