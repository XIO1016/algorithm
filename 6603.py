import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    lst = list(map(int, input().strip().split()))
    k = lst[0]
    lst = lst[1:]
    if k == 0 and len(lst) == 0:
        break
    for i in combinations(lst, 6):
        print(" ".join(list(map(str, i))))
    print("")
