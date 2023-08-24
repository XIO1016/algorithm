import heapq
import sys

input = sys.stdin.readline

n = int(input())
oil = [list(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())
oil.append([l, 0])
oil.sort()

heap = []
ans = 0
for i in range(len(oil)):
    if p - oil[i][0] < 0:
        while heap:
            p -= heapq.heappop(heap)
            ans += 1
            if p - oil[i][0] >= 0:
                break
    if len(heap) == 0 and p - oil[i][0] < 0:
        print(-1)
        break
    else:
        heapq.heappush(heap, -oil[i][1])
