import sys

input = sys.stdin.readline
n = input().strip()

i = 0
while True:
    i += 1
    num = str(i)
    while len(num) and len(n):
        if num[0] == n[0]:
            n = n[1:]
        num = num[1:]
    if n == '':
        print(i)
        break
