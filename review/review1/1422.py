import sys

input = sys.stdin.readline

k, n = map(int, input().split())

num = []
num1 = []
for _ in range(k):
    a = input().strip()
    num.append(a)
    num1.append(int(a))

plus = max(num1)
for _ in range(n - k):
    num.append(str(plus))

num.sort(key=lambda x: x * 10, reverse=True)
print(''.join(num))
