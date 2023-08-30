import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

s = 0
for i in range(n):
    s += 1
    if a[i] > b:
        a[i] -= b
        s += a[i] // c
        a[i] = a[i] % c
        if a[i] > 0:
            s += 1
    else:
        continue

print(s)
