import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    m = 0
    s = 0
    for i in range(n - 1, -1, -1):
        if m < arr[i]:
            m = arr[i]
        else:
            s += m - arr[i]
    print(s)
