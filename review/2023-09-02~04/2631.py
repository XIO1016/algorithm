import sys

input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
d = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i):
        if arr[j] < arr[i]:
            d[i] = max(d[j] + 1, d[i])

print(n - max(d))
