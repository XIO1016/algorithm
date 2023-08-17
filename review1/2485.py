import sys

input = sys.stdin.readline

n = int(input())
tree = [int(input()) for _ in range(n)]


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


arr = []
for i in range(n - 1):
    arr.append(tree[i + 1] - tree[i])

m = arr[0]

for i in range(n - 2):
    m = gcd(m, arr[i + 1])
s = 0
for i in range(n - 1):
    s += arr[i] // m - 1
print(s)
