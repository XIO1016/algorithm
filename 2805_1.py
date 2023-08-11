import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tree = list(map(int, input().split()))

left, right = 0, max(tree)
while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in tree:
        if i > mid:
            s += i - mid
    if s > m:
        left = mid + 1
    elif s < m:
        right = mid - 1
    else:
        break
print((left + right) // 2)
