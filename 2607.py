import sys

input = sys.stdin.readline
n = int(input())

a = list(input().strip())

ans = 0
for i in range(n - 1):
    compare = a[:]
    word = input().strip()
    cnt = 0
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    if cnt < 2 and len(compare) < 2:
        ans += 1

print(ans)
