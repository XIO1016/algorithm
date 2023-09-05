import sys

input = sys.stdin.readline

n = int(input())

row = [0] * n
visited = [0] * n
ans = 0


def check(x):
    for i in range(x):
        if row[i] == row[x] or abs(x - i) == abs(row[x] - row[i]):
            return False
    return True


def dfs(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            if not visited[i]:
                row[x] = i
                if check(x):
                    visited[i] = 1
                    dfs(x + 1)
                    visited[i] = 0


dfs(0)
print(ans)
