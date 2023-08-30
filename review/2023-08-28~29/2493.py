import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = []
ans = [0] * n

for i in range(n):
    while stack:
        if stack[-1][1] < arr[i]:
            stack.pop()
        else:
            ans[i] = stack[-1][0] + 1
            break
    stack.append((i, arr[i]))

print(ans)
