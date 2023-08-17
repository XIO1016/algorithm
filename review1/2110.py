import sys

input = sys.stdin.readline

n, c = map(int, input().split())

home = [int(input()) for _ in range(n)]
home.sort()

left, right = 0, home[-1] - home[0]
while left <= right:
    mid = (left + right) // 2
    s = 1
    last = home[0]
    for i in home:
        if i - last >= mid:
            last = i
            s += 1
    if s >= c:
        left = mid + 1
    else:
        right = mid - 1
print(right)
