import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    arr = list(map(int, input().split()))
    for x in arr:
        if len(heap) < n:
            heapq.heappush(heap, x)
        else:
            if heap[0] < x:
                heapq.heappop(heap)
                heapq.heappush(heap, x)

print(heap[0])
