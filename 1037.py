import sys

input = sys.stdin.readline

cnt = int(input())
lst = list(map(int, input().split()))
lst.sort()

if len(lst) % 2 == 0:
    print(lst[0] * lst[-1])
else:
    mid = len(lst) // 2
    print(lst[mid] * lst[mid])
