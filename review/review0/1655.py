import heapq
import sys

input = sys.stdin.readline

n = int(input())

left = []
right = []

for _ in range(n):
    x = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)
    if right and -left[0] > right[0]:
        a = heapq.heappop(left)
        b = heapq.heappop(right)
        heapq.heappush(left, -b)
        heapq.heappush(right, -a)
    print(-left[0])
