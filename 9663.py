import sys

input = sys.stdin.readline

n = int(input())

row = [0] * n
result = 0
visited = [False] * n


def not_adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            if visited[i]:
                continue
            row[x] = i
            if not_adjacent(x):
                visited[i] = True
                dfs(x + 1)
                visited[i] = False


dfs(0)
print(result)
