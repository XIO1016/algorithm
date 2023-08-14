import sys

input = sys.stdin.readline
n = int(input())

body = [list(input().strip()) for _ in range(n)]

x = 0
y = 0
for i in range(n):
    for j in range(n):
        if body[i][j] == '*':
            if i + 1 < n and i - 1 >= 0 and body[i - 1][j] == '*' and body[i + 1][j] == '*':
                if j + 1 < n and j - 1 >= 0 and body[i][j - 1] == '*' and body[i][j + 1] == '*':
                    print(i + 1, j + 1)
                    x = i
                    y = j

s1 = 0
for i in range(y):
    if body[x][i] == '*':
        s1 += 1

s2 = 0
for i in range(y + 1, n):
    if body[x][i] == "*":
        s2 += 1

x1 = 0
y1 = 0
for i in range(x + 1, n):
    if body[i][y] == '*':
        x1 += 1
        y1 = i

s3 = 0
for i in range(n - 1, y1, -1):
    if body[i][y - 1] == '*':
        s3 += 1
s4 = 0
for i in range(n - 1, y1, -1):
    if body[i][y + 1] == '*':
        s4 += 1

print(s1, s2, x1, s3, s4)
