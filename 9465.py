import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(2)]
    if n > 1:
        d[0][1] += d[1][0]
        d[1][1] += d[0][0]

    for j in range(2, n):
        d[0][j] += max(d[1][j - 1], d[1][j - 2])
        d[1][j] += max(d[0][j - 1], d[0][j - 2])
    print(max(d[0][n - 1], d[1][n - 1]))
