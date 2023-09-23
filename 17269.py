import sys

input = sys.stdin.readline
n, m = map(int, input().split())

a, b = input().strip().split()

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

ab = ""
end = min(n, m)
for i in range(end):
    ab += a[i] + b[i]
ab += a[end:] + b[end:]

lst = [alp[ord(i) - ord('A')] for i in ab]

for i in range(n + m - 2):
    for j in range(n + m - 1 - i):
        lst[j] += lst[j + 1]
print("{}%".format(lst[0] % 10 * 10 + lst[1] % 10))
