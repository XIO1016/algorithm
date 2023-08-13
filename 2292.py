import sys

input = sys.stdin.readline

n = int(input())
ans = 1
while n > 1:
    n -= ans * 6
    ans += 1
print(ans)

# 66 - 6 - 12 - 18 - 24 - 30
