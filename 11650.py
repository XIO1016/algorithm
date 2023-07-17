import sys

input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for i in range(n)]
lst.sort(key=lambda x: (x[0], x[1]))
for i in lst:
    print(" ".join(map(str, i)))
