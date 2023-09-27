import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

a = list(map(int, input().split()))
a.reverse()

q = deque()
for i in range(n):
    if a[i] == 1:
        q.appendleft(i + 1)
    elif a[i] == 2:
        q.insert(1, i + 1)
    else:
        q.append(i + 1)

print(*q)
