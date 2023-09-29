s = list(input())
a_cnt = s.count('a')

left = 0

ans = int(1e9)
while left < len(s):
    right = left + a_cnt
    if right > len(s):
        tmp = s[left:] + s[:right - len(s)]
    else:
        tmp = s[left:right]
    ans = min(ans, tmp.count("b"))
    left += 1
print(ans)
