import sys

input = sys.stdin.readline

k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]

left, right = 1, max(l)

while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in l:
        s += i // mid
    if s >= n:
        left = mid + 1
    elif s < n:
        right = mid - 1
print(right)
