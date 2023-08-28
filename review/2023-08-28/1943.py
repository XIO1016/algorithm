import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    coins = {}
    target = 0
    for _ in range(n):
        a, b = map(int, input().split())
        coins[a] = b
        target += a * b
    if target % 2 != 0:
        print(0)
        break
    target //= 2
    d = [1] + [0] * target
    for c in coins:
        for money in range(target, c - 1, -1):
            if d[money - c]:
                for i in range(coins[c]):
                    if money + i * c <= target:
                        d[money + i * c] = 1
