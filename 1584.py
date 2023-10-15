import sys

input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())))
if n > 2:
    ans = 2
    for start in range(n - 2):
        end = start + 2
        while True:
            if arr[start] + arr[start + 1] > arr[end]:
                ans = max(ans, end - start + 1)
                end += 1
                if end == n: break
            else:
                break
    print(ans)
else:
    print(n)
