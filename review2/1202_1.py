import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []
for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))
bag = [int(input()) for _ in range(k)]
bag.sort()
temp = []
ans = 0
for b in bag:
    while jewel and jewel[0][0] <= b:
        m, v = heapq.heappop(jewel)
        heapq.heappush(temp, -v)
    if temp:
        ans -= heapq.heappop(temp)
print(ans)
