import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewel, (m, v))
bag = [int(input()) for _ in range(k)]
bag.sort()

ans = 0
temp = []
for b in bag:
    while jewel and jewel[0][0] <= b:
        m, v = heapq.heappop(jewel)
        heapq.heappush(temp, -v)
    if temp:
        ans -= heapq.heappop(temp)
print(ans)
