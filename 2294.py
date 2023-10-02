import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]
d = [int(1e9)] * (k + 1)
d[0] = 0

for a in coin:
    for i in range(a, k + 1):
        d[i] = min(d[i], d[i - a] + 1)
if d[k] == int(1e9):
    print(-1)
else:
    print(d[k])
