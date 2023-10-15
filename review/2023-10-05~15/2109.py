import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

heap = []
for a in arr:
    heapq.heappush(heap, a[0])
    if len(heap) > a[1]:
        heapq.heappop(heap)
print(sum(heap))
