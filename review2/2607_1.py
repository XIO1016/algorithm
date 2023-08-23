import sys

input = sys.stdin.readline

n = int(input())

word = input().strip()

ans = 0
for _ in range(n - 1):
    compare = word[:]
    x = input().stip()
    cnt = 0
    for i in x:
        if i in compare:
            compare.remove(i)
        else:
            cnt += 1
    if cnt < 2 and len(compare) < 2:
        ans += 1
print(ans)
