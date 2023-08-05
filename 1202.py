import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

jewel = []
for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))
bags = [int(input()) for _ in range(k)]
bags.sort()

ans = 0
temp = []
for b in bags:
    while jewel and b >= jewel[0][0]:
        w, c = heapq.heappop(jewel)
        heapq.heappush(temp, -c)
    if temp:
        ans -= heapq.heappop(temp)

print(ans)
