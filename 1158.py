import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = [i + 1 for i in range(n)]
start = 0
ans = []
while len(lst) > 0:
    start = (start + k - 1) % len(lst)
    ans.append(lst[start])
    lst.remove(lst[start])
print("<", ", ".join(map(str, ans)), ">", sep="")
