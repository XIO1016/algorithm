import sys

input = sys.stdin.readline

n = int(input())
bulb = list(map(int, input().split()))
target = list(map(int, input().split()))


def change(a, b):
    a1 = a[:]
    cnt = 0
    for i in range(1, n):
        if a1[i - 1] == b[i - 1]:
            continue
        cnt += 1
        for j in range(i - 1, i + 2):
            if j < n:
                a1[j] = 1 - a1[j]
    if a1 == b:
        return cnt
    else:
        return 1e9


result = change(bulb, target)
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]

result = min(result, change(bulb, target))
if result != 1e9:
    print(result)
else:
    print(-1)
