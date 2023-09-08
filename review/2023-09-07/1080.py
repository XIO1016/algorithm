import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]


def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a[x][y] = 1 - a[x][y]


cnt = 0
if (n < 3 or m < 3) and a != b:
    cnt = -1
else:
    for r in range(n - 2):
        for c in range(m - 2):
            if a[r][c] != b[r][c]:
                cnt += 1
                flip(r, c)
if cnt != -1:
    if a != b:
        cnt = -1
print(cnt)
