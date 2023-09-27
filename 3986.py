import sys

input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    stack = []
    arr = list(input().strip())
    for i in arr:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        ans += 1
print(ans)
