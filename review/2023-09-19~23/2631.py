import sys

input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
d = [1] * (n + 1)

for i in range(n):
    for j in range(n):
        if arr[i] < arr[j]:
            d[i] = max(d[i], d[j] + 1)
print(n - max(d))
