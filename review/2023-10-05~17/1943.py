import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    total = 0
    coin = {}
    for _ in range(n):
        a, b = map(int, input().split())
        coin[a] = b
        total += a * b
    if total % 2 != 0:
        print(0)
        continue
    total //= 2
    d = [1] + [0] * total
    for c in coin:
        for money in range(total, c - 1, -1):
            if d[money - c]:
                for i in range(coin[c]):
                    if money + c * i <= total:
                        d[money + c * i] = 1
    print(d[total])
