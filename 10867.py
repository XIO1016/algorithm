import sys

input = sys.stdin.readline
n = int(input())
lst = set(list(map(int, input().split())))
print(" ".join(map(str, sorted(lst))))
