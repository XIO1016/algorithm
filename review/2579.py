import sys

input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]

d = [0] * n

if n <= 2:
    print(sum(step))
else:
    d[0] = step[0]
    d[1] = step[0] + step[1]
    d[2] = max(step[0] + step[2], step[1] + step[2])
    for i in range(3, n):
        d[i] = max(d[i - 3] + step[i - 1] + step[i], d[i - 2] + step[i])

print(d[-1])
