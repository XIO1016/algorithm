n, r, c = map(int, input().split())

ans = 0
while n:
    n -= 1
    if r < 2 ** n and c < 2 ** n:
        ans += (2 ** n) * (2 ** n) * 0
    elif r < 2 ** n and c >= 2 ** n:
        ans += (2 ** n) * (2 ** n) * 1
        c -= 2 ** n
    elif c < 2 ** n <= r:
        ans += (2 ** n) * (2 ** n) * 2
        r -= 2 ** n
    else:
        ans += (2 ** n) * (2 ** n) * 3
        c -= 2 ** n
        r -= 2 ** n
print(ans)
