for _ in range(3):
    n = int(input())
    coin = {}
    target = 0
    for _ in range(n):
        a, b = map(int, input().split())
        coin[a] = b
        target += a * b
    if target % 2 != 0:
        print(0)
        continue
    target //= 2
    d = [1] + [0] * target
    for c in coin:
        for money in range(target, c - 1, -1):
            if d[money - c]:
                for j in range(coin[c]):
                    if money + c * j <= target:
                        d[money + c * j] = 1
    print(d[target])
