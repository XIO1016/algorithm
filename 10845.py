import sys

input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    i = input().split()
    cmd = i[0]
    if cmd == "push":
        q.insert(0, i[1])
    elif cmd == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    elif cmd == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
