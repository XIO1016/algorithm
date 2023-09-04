import sys

input = sys.stdin.readline

num = input().strip()

i = 0
while len(num):
    i += 1
    n = str(i)
    while len(n) and len(num):
        if n[0] == num[0]:
            num = num[1:]
        n = n[1:]
    if num == '':
        print(i)
        break
