import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    lst = list(input().strip())
    stack = []
    isVPS = True
    for i in lst:

        if i == "(":
            stack.append(i)
        else:
            if not stack:
                isVPS = False
                break
            else:
                stack.pop()

    if isVPS and not stack:
        print("YES")
    else:
        print("NO")
