import sys

input = sys.stdin.readline

k, n = map(int, input().split())

plus = 0
num = []
for _ in range(k):
    a = input().strip()
    num.append(a)
    plus = max(plus, int(a))

for _ in range(n - k):
    num.append(str(plus))

num.sort(key=lambda x: x * 10, reverse=True)

print("".join(num))
