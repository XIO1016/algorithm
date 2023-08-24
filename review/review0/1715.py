import heapq
import sys

input = sys.stdin.readline

n = int(input())

card = []
for _ in range(n):
    heapq.heappush(card, int(input()))
s = 0
while len(card) > 1:
    temp = heapq.heappop(card) + heapq.heappop(card)
    s += temp
    heapq.heappush(card, temp)
print(s)
