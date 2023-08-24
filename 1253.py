import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
cnt = 0
a.sort()
for i in range(n):
    tmp = a[:i] + a[i + 1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        s = tmp[left] + tmp[right]
        if s == a[i]:
            cnt += 1
            break
        elif s < a[i]:
            left += 1
        else:
            right -= 1
print(cnt)
