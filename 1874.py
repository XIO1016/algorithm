import sys

input = sys.stdin.readline

n = int(input())
stack = []
op = []
cnt = 1
is_exist = True

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        cnt += 1
        op.append("+")
    if stack[-1] == num:
        stack.pop()
        op.append("-")
    else:
        is_exist = False
        break
if not is_exist:
    print("NO")
else:
    print("\n".join(op))
