import sys

input = sys.stdin.readline
r, c, w = map(int, input().split())
n = r + w - 1
d = [[0] * n for _ in range(n)]
d[0][0] = 1
for i in range(1, n):
    d[i][0] = 1
    d[i][i] = 1
for i in range(2, n):
    for j in range(1, i):
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j]
ans = 0
for i in range(w):
    for j in range(i + 1):
        ans += d[i + r - 1][j + c - 1]
print(ans)
