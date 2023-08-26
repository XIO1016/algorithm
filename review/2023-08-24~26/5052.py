import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    real = False
    for i in range(n - 1):
        if arr[i] in arr[i + 1][:len(arr) + 1]:
            print("NO")
            real = True
            break
    if real == False:
        print("YES")
