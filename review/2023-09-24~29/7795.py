from bisect import bisect_left

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    s = 0
    for i in a:
        s += bisect_left(b, i)
    print(s)
