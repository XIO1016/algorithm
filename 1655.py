import heapq
import sys

input = sys.stdin.readline

n = int(input())

left = []
right = []
for _ in range(n):
    x = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-x, x))
    else:
        heapq.heappush(right, (x, x))
    if right and left[0][1] > right[0][1]:
        n = heapq.heappop(right)[0]
        m = heapq.heappop(left)[1]
        heapq.heappush(right, (m, m))
        heapq.heappush(left, (-n, n))
    print(left[0][1])
