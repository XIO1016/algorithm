import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
mn, mx = min(a), max(a)

ans = n + 1
mni, mxi = -1, -1
for idx, num in enumerate(a):
    if num == mn:
        mni = idx
        if mxi != -1:
            ans = min(ans, abs(mxi - mni))
    if num == mx:
        mxi = idx
        if mni != -1:
            ans = min(ans, abs(mxi - mni))

print(ans + 1)
