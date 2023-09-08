import sys
from bisect import bisect_left

input = sys.stdin.readline

n, h = map(int, input().split())

down = []
up = []

for i in range(n):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()
cnt = 1
ans = float('inf')
for i in range(1, h + 1):
    t, b = bisect_left(up, (h + 1) - i), bisect_left(down, i)
    total = n - (t + b)
    if total < ans:
        ans = total
        cnt = 1
    elif ans == total:
        cnt += 1
print(ans, cnt)
