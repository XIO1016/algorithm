import sys

input = sys.stdin.readline

n, c = map(int, input().split())

x = [int(input()) for _ in range(n)]
x.sort()
left, right = 0, x[-1] - x[0]

ans = 0
while left <= right:
    mid = (left + right) // 2
    s = 1
    last = x[0]
    for i in x:
        if i - last >= mid:
            s += 1
            last = i
    if s >= c:
        left = mid + 1
    else:
        right = mid - 1

print(right)
