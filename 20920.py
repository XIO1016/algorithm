import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = {}
for _ in range(n):
    x = input().strip()
    if len(x) < m:
        continue
    try:
        arr[x] += 1
    except:
        arr[x] = 1
ans = sorted(arr.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in range(len(ans)):
    print(ans[i][0])
