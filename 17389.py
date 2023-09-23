import sys

input = sys.stdin.readline

n = int(input())
s = list(input())
bonus = 0
ans = 0
for i in range(n):
    if s[i] == "O":
        ans += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(ans)
