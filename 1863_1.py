import sys

input = sys.stdin.readline

n = int(input())

ans = 0
stack = []
for _ in range(n):
    x, y = map(int, input().split())
    while len(stack) > 0 and stack[-1] > y:
        ans += 1
        stack.pop()
    if len(stack) > 0 and stack[-1] == y:
        continue
    stack.append(y)

while len(stack) > 0:
    if stack[-1] > 0:
        ans += 1
    stack.pop()
print(ans)
