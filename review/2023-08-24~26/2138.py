import sys

input = sys.stdin.readline

n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))


def change(a, b):
    a1 = a[:]
    press = 0
    for i in range(1, n):
        if a1[i - 1] == b[i - 1]:
            continue
        press += 1
        for j in range(i - 1, i + 2):
            if j < n:
                a1[j] = 1 - a1[j]
    if a1 == b:
        return press
    else:
        return 1e9


result = change(bulb, target)

bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
result = min(result, change(bulb, target) + 1)
if result != 1e9:
    print(result)
else:
    print(-1)
