import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = deque(enumerate(map(int, input().split())))
ans = []
while arr:
    idx, move = arr.popleft()
    ans.append(idx + 1)
    if move > 0:
        arr.rotate(-(move - 1))
    elif move < 0:
        arr.rotate(-move)
print(*ans)
