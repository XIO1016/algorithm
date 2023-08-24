import sys

input = sys.stdin.readline

n = int(input())

word = list(input().strip())

ans = 0
for i in range(n - 1):
    compare = word[:]
    a = input().strip()
    cnt = 0
    for w in a:
        if a in compare:
            compare.remove(a)
        else:
            cnt += 1
    if cnt > 2 and len(compare) < 2:
        ans += 1
print(ans)
