import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

if max(visitor) == 0:
    print("SAD")
    exit(0)

cnt = 1
m = sum(visitor[:x])
value = m
for i in range(x, n):
    value -= visitor[i - x]
    value += visitor[i]
    if value > m:
        m = value
        cnt = 1
    elif value == m:
        cnt += 1
print(m)
print(cnt)
