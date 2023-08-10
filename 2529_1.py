import sys

input = sys.stdin.readline

k = int(input())

arr = list(input().strip().split())

m, n = "", ""


def check(a, b, c):
    if c == "<":
        return a < b
    else:
        return a > b


visited = [0] * 10


def dfs(idx, num):
    global m, n
    if idx == k + 1:
        if len(n) == 0:
            n = num
        else:
            m = num
        return
    for i in range(10):
        if visited[i] == 0:
            if idx == 0 or check(num[-1], str(i), arr[idx - 1]):
                visited[i] = 1
                dfs(idx + 1, num + str(i))
                visited[i] = 0


dfs(0, "")
print(m)
print(n)
