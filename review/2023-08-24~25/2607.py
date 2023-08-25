import sys

input = sys.stdin.readline

n = int(input())
word = list(input().strip())
ans = 0
for _ in range(n - 1):
    target = word[:]
    a = input().strip()
    cnt = 0
    for i in a:
        if i in target:
            target.remove(i)
        else:
            cnt += 1
    if cnt < 2 and len(target) < 2:
        ans += 1
print(ans)
