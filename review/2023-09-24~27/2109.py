import heapq

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])

heap = []
for p, d in arr:
    heapq.heappush(heap, p)
    if d < len(heap):
        heapq.heappop(heap)
print(sum(heap))
