import sys

input = sys.stdin.readline

n = int(input())
rq = list(map(int, input().split()))
m = int(input())

if sum(rq) <= m:
    print(max(rq))
    exit(0)

left, right = 1, max(rq)
while left <= right:
    mid = (left + right) // 2
    s = 0
    for i in rq:
        if i > mid:
            s += mid
        else:
            s += i
    if s > m:
        right = mid - 1
    else:
        left = mid + 1

print(right)
