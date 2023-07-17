import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
A.sort()

for i in B:
    left, right = 0, n - 1
    isExist = False
    while left <= right:
        mid = (left + right) // 2
        if i == A[mid]:
            isExist = True
            print(1)
            break
        elif i < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if not isExist:
        print(0)
