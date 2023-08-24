import sys

input = sys.stdin.readline

n = int(input())

tree = [int(input()) for _ in range(n)]

tree.sort()


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


arr = []
for i in range(n - 1):
    arr.append(tree[i + 1] - tree[i])

g = arr[0]
for i in range(1, len(arr)):
    g = gcd(g, arr[i])

ans = 0
for i in range(len(arr)):
    ans += arr[i] // g - 1

print(ans)
