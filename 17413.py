import sys

input = sys.stdin.readline
s = input().strip()
stack = ""
tag = False
ans = ""
for i in s:
    if i == "<":
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        tag = False
        ans += i
        continue
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue

    if tag:
        ans += i
    else:
        stack += i
print(ans + stack[::-1])
