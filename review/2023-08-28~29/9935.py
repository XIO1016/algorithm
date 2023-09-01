import sys

input = sys.stdin.readline

s = input().strip()
bomb = input().strip()

stack = []
l = len(bomb)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-l:]) == bomb:
        for _ in range(l):
            stack.pop()
