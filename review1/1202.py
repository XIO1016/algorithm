import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
jewel = []
for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))
weight = [int(input()) for _ in range(k)]

weight.sort()

s = 0
temp = []
for w in weight:
    while jewel and jewel[0][0] <= w:
        w, c = heapq.heappop(jewel)
        heapq.heappush(temp, -c)
    if temp:
        s -= heapq.heappop(temp)
print(s)
