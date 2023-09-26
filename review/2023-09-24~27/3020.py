from bisect import bisect_left

n, h = map(int, input().split())

top = []
down = []
for i in range(n):
    a = int(input())
    if i % 2 == 0:
        down.append(a)
    else:
        top.append(a)
down.sort()
top.sort()

cnt = 1
ans = int(1e9)
for i in range(1, h + 1):
    t, b = bisect_left(top, (h + 1) - i), bisect_left(down, i)
    total = n - (t + b)
    if total < ans:
        ans = total
        cnt = 1
    elif total == ans:
        cnt += 1
print(ans, cnt)
