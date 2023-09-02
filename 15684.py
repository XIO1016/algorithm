import sys

input = sys.stdin.readline


def check():
    for i in range(1, n + 1):
        tmp = i
        for j in range(1, h + 1):
            if graph[j][tmp] == 1:
                tmp += 1
            elif graph[j][tmp] == 2:
                tmp -= 1
        if tmp != i:
            return False
    return True


def checkLine(x, y):
    if graph[y][x] == 0 and graph[y][x + 1] == 0:
        return True
    return False


def dfs(cnt):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(1, n):
        ch = 0
        for j in range(1, h + 1):
            if ch and checkLine(i, j):
                continue
            else:
                ch = 0
            if checkLine(i, j):
                graph[j][i] = 1
                graph[j][i + 1] = 2
                dfs(cnt + 1)
                graph[j][i] = 0
                graph[j][i + 1] = 0
                ch = 1


n, m, h = map(int, input().split())
graph = [[0] * 12 for _ in range(31)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[a][b + 1] = 2

ans = 4
dfs(0)
print(ans if ans != 4 else -1)
