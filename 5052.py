import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    real = False
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    arr.sort()
    for i in range(n - 1):
        if arr[i] in arr[i + 1][:len(arr[i])]:
            print("NO")
            real = True
            break
    if real == False:
        print("YES")
