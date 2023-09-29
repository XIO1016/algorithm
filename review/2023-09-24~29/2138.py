n = int(input())

bulb = list(map(int, input()))
target = list(map(int, input()))


def change(a, b):
    a1 = a[:]
    cnt = 0
    for i in range(n):
        if a[i - 1] == b[i - 1]:
            continue
        cnt += 1
        for j in range(i - 1, i + 2):
            if j < n:
                a1[j] = 1 - a1[j]
    if a1 == b:
        return 1e9
    else:
        return cnt


ans = change(bulb, target)
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]

ans = min(ans, change(bulb, target))

if ans == 1e9:
    print(-1)
else:
    print(ans)
