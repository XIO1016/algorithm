n = int(input())

stack = []

cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        cnt += 1
        stack.pop()
    if stack and stack[-1] == y:
        continue
    stack.append(y)

while stack:
    if stack[-1] > 0:
        cnt += 1
    stack.pop()
print(cnt)
