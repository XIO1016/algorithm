import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

T = int(input())


def dfs(a):
    global ans
    visited[a] = 1
    cycle.append(a)
    num = arr[a]
    if visited[num] == 1:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - len(ans))
