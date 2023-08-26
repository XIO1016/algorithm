import math
import sys

input = sys.stdin.readline

s = list(input().strip())

cnt1 = s.count('a')
ans = math.inf

left = 0

while left < len(s):
    right = left + cnt1
    if right > len(s):
        temp = s[left:len(s)] + s[:right - len(s)]
    else:
        temp = s[left:right]
    ans = min(ans, temp.count('b'))
    left += 1
