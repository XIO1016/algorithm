import sys

input = sys.stdin.readline

n, m, l, k = map(int, input().split())

star = []
for _ in range(k):
    x, y = map(int, input().split())
    star.append((x, y))

ans = k
for i, _ in star:
    for _, j in star:
        tmp = k
        for a, b in star:
            if i <= a <= i + l and j <= b <= j + l:
                tmp -= 1
        ans = min(ans, tmp)
print(ans)
