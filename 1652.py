import sys

input = sys.stdin.readline

n = int(input())

graph = [list(input().strip()) for _ in range(n)]

ans = [0, 0]
for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
        if graph[i][j] == ".":
            cnt1 += 1
        else:
            cnt1 = 0
        if cnt1 == 2:
            ans[0] += 1

        if graph[j][i] == ".":
            cnt2 += 1
        else:
            cnt2 = 0
        if cnt2 == 2:
            ans[1] += 1
print(*ans)
