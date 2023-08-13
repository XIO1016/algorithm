import sys

input = sys.stdin.readline

n, l = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

start = a[0]

cnt = 1

for location in a[1:]:
    if location in range(start, start + l):
        continue
    else:
        start = location
        cnt += 1
print(cnt)
