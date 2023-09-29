n = int(input())

row = [0] * n
ans = 0
visited = [0] * n


def not_adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            if visited[i]:
                continue
            row[x] = i
            if not_adjacent(x):
                visited[i] = 1
                dfs(x + 1)
                visited[i] = 0


dfs(0)
print(ans)
