import sys

input = sys.stdin.readline
s = input().strip()
e = input().strip()

stack = []
l = len(e)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-l:]) == e:
        for _ in range(l):
            stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))
