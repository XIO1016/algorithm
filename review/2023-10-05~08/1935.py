import sys

input = sys.stdin.readline

n = int(input())
s = list(input().strip())

stack = []
num = [int(input()) for _ in range(n)]
for i in s:
    print(stack)
    if i.isalpha():
        stack.append(num[ord(i) - ord('A')])
    else:
        a = stack.pop()
        ans = stack.pop()
        if i == '+':
            ans += a
        elif i == '-':
            ans -= a
        elif i == '*':
            ans *= a
        else:
            ans /= a
        stack.append(ans)
print('%0.2f' % stack[-1])
