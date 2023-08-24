import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

m = arr[0]
for i in range(1, n):
    m = max(m, arr[i] * (i + 1))

print(m)
