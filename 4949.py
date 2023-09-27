import sys

input = sys.stdin.readline
while True:
    arr = list(input())
    stack = []
    if arr[0] == '.':
        break
    for i in arr:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack):
        print('no')
    else:
        print('yes')
