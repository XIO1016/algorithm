import sys

input = sys.stdin.readline

n = int(input())
qty = [int(input()) for _ in range(n)]

d = [0] * (n)
d[0] = qty[0]
if n > 1:
    d[1] = qty[0] + qty[1]
if n > 2:
    d[2] = max(d[1], qty[1] + qty[2], qty[0] + qty[2])
for i in range(3, n):
    d[i] = max(d[i - 1], d[i - 3] + qty[i - 1] + qty[i], d[i - 2] + qty[i])
print(d[-1])
print(d)
