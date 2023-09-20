import math
import sys

input = sys.stdin.readline
s = list(input().strip())
a_cnt = s.count('a')

ans = math.inf
left = 0

while left < len(s):
    right = left + a_cnt
    if right > len(s):
        temp = s[left:] + s[:right - len(s)]
    else:
        temp = s[left:right]
    ans = min(ans, temp.count('b'))
    left += 1
print(ans)
