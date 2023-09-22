import sys
from bisect import bisect

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 0
    for i in a:
        ans += bisect(b, i - 1)
    print(ans)
