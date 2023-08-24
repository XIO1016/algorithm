import sys

input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

left, right = 0, x[-1] - x[0]
while left <= right:
    mid = (left + right) // 2  # 공유기 간 거리
    last = x[0]
    s = 1
    for i in x:
        if i - last >= mid:
            last = i
            s += 1
    if s >= c:
        left += 1
    else:
        right -= 1
print(right)
