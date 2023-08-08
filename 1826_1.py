import heapq
import sys

input = sys.stdin.readline

n = int(input())
station = [list(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())

station.append([l, 0])
station.sort()
heap = []
ans = 0
for i in range(n + 1):
    if p - station[i][0] < 0:
        while heap:
            p += -heapq.heappop(heap)
            ans += 1
            if p - station[i][0] >= 0:
                break
    if not heap and p - station[i][0] < 0:
        ans = -1
        break
    else:
        heapq.heappush(heap, -station[i][1])

print(ans)
