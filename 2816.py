import sys

input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

idx1, idx2 = arr.index('KBS1'), arr.index('KBS2')

if idx1 > idx2:
    idx2 += 1

print('1' * idx1 + '4' * idx1 + '1' * idx2 + '4' * (idx2 - 1))
