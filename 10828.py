import sys

input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    i = input().split()
    cmd = i[0]
    if cmd == "push":
        stack.append(i[1])
    elif cmd == "pop":
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
