import heapq
import sys

input = sys.stdin.readline

n = int(input())
station = [list(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())

ans = 0
station.append([l, 0])
station.sort()
heap = []

for i in range(len(station)):
    if p - station[i][0] < 0:
        while heap:
            p += -heapq.heappop(heap)
            ans += 1
            if p - station[i][0] >= 0:
                break
    if len(heap) == 0 and p - station[i][0] < 0:
        ans = -1
        break
    else:
        heapq.heappush(heap, -station[i][1])

print(ans)
