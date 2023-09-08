import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(2, n):
        ans = max(ans, abs(l[i] - l[i - 2]))
    print(ans)
