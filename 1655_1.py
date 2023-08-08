import heapq
import sys

input = sys.stdin.readline

n = int(input())

left = []
right = []

for i in range(n):
    v = int(input())
    if len(right) == len(left):
        heapq.heappush(left, -v)
    else:
        heapq.heappush(right, v)
    if right and -left[0] > right[0]:
        l = -heapq.heappop(left)
        r = heapq.heappop(right)
        heapq.heappush(right, l)
        heapq.heappush(left, -r)

    print(-left[0])
