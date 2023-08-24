import sys

input = sys.stdin.readline

n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]

home.sort()
left, right = 0, home[-1] - home[0]

while left <= right:
    mid = (left + right) // 2
    last = home[0]
    s = 1
    for i in home:
        if i - last >= mid:
            last = i
            s += 1
    if s >= c:
        left = mid + 1
    elif s < c:
        right = mid - 1
print(right)
