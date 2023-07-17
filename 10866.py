import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
dq = deque()
for _ in range(n):
    i = input().split()
    cmd = i[0]
    if cmd == "push_front":
        dq.appendleft(i[1])
    elif cmd == "push_back":
        dq.append(i[1])
    elif cmd == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif cmd == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif cmd == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
