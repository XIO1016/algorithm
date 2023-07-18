import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = list(input().strip())
    n = int(input())
    x = deque(input().strip()[1:-1].split(","))
    order_origin = True
    is_error = False
    if n == 0:
        x = []
    for i in p:
        if i == "R":
            order_origin = not order_origin
        elif i == "D":
            if not x:
                is_error = True
                break
            elif order_origin:
                x.popleft()
            elif not order_origin:
                x.pop()
    if is_error:
        print("error")
    elif order_origin:
        print("[", ",".join(x), "]", sep="")
    else:
        x.reverse()
        print("[", ",".join(x), "]", sep="")
