import sys

input = sys.stdin.readline

k, n = map(int, input().split())

num = []
plus = 0
for _ in range(k):
    temp = input().strip()
    num.append(temp)
    plus = max(plus, int(temp))

for i in range(n - k):
    num.append(str(plus))

num.sort(key=lambda x: x * 10, reverse=True)
ans = ''.join(num)
print(int(ans))
