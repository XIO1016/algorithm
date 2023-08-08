import sys

input = sys.stdin.readline

n = int(input())

if n < 10:
    a = '0' + str(n)
else:
    a = str(n)

cnt = 0
while 1:
    a = a[1] + str(int(a[0]) + int(a[1]))[-1]
    cnt += 1
    if int(a) == n:
        break
print(cnt)
