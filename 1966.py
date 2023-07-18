import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    importance = deque(list(map(int, input().split())))
    ans = 0
    while importance:
        best = max(importance)
        front = importance.popleft()
        m -= 1
        if best == front:
            ans += 1
            if m < 0:
                print(ans)
                break
        else:
            importance.append(front)
            if m < 0:
                m = len(importance) - 1
