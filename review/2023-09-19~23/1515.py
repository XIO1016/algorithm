import sys

input = sys.stdin.readline
num = input().strip()
i = 0
while True:
    i += 1
    n = str(i)
    while len(num) > 0 and len(n) > 0:
        if num[0] == n[0]:
            num = num[1:]
        n = n[1:]
    if n == '':
        print(i)
        break
