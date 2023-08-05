import heapq
import sys

input = sys.stdin.readline

n = int(input())

card = []
for _ in range(n):
    heapq.heappush(card, int(input()))
if n == 1:
    print(0)
    exit(0)

cnt = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    cnt += a + b
    heapq.heappush(card, a + b)

print(cnt)
