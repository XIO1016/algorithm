import sys

input = sys.stdin.readline

s = list(input().strip())

a_cnt = s.count('a')
INF = float('inf')

left = 0
ans = INF
while left < len(s):
    right = left + a_cnt
    if right > len(s):
        temp = s[left:] + s[:right - len(s)]
    else:
        temp = s[left:right]
    ans = min(ans, s.count('b'))
    left += 1
print(ans)
