import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
d = [1] * n
d[0] = a[0]
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j] + a[i])
        else:
            d[i] = max(d[i], a[i])
print(max(d))
