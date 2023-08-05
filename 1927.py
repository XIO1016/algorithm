import heapq
import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(arr))
        except:
            print(0)
    else:
        heapq.heappush(arr, x)
