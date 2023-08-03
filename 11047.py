import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

a.sort(reverse=True)

ans = 0
for i in a:
    ans += k // i
    k = k % i
print(ans)
