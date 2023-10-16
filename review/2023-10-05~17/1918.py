import sys

input = sys.stdin.readline

s = list(input().strip())
stack = []

ans = ''
for i in s:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' and i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)

while stack:
    ans += stack.pop()
print(ans)
