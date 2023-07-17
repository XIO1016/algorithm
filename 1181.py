import sys

input = sys.stdin.readline
n = int(input())
lst = list(set(input().strip() for _ in range(n)))
print("\n".join(sorted(lst, key=lambda x: (len(x), x))))
