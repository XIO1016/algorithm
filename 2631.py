import sys

input = sys.stdin.readline

n = int(input())
children = [0] + [int(input()) for _ in range(n)]
d = [1] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, i):
        if children[j] < children[i]:
            d[i] = max(d[i], d[j] + 1)
print(n - max(d))
