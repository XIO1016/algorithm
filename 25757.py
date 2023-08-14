import sys

input = sys.stdin.readline

n, game = input().strip().split()
n = int(n)
name = [input().strip() for _ in range(n)]

name = set(name)

if game == 'Y':
    print(len(name))
elif game == 'F':
    print(len(name) // 2)
else:
    print(len(name) // 3)
