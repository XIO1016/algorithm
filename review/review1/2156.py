import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
d = [0] * n
if n == 1:
    print(arr[0])
    exit(0)
d[0] = arr[0]
d[1] = arr[0] + arr[1]
for i in range(2, n):
    d[i] = max(d[i - 2] + arr[i], d[i - 3] + arr[i - 1] + arr[i], d[i - 1])

print(d[n - 1])
