import sys

input = sys.stdin.readline

p = int(input())
for _ in range(p):
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                ans += 1
                arr[j], arr[i] = arr[i], arr[j]
    print(arr[0], ans)
