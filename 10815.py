import sys

input = sys.stdin.readline
n = int(input())
A = sorted(map(int, input().split()))
m = int(input())
B = map(int, input().split())

arr = []
for i in B:
    left, right = 0, n - 1
    isExist = False
    while left <= right:
        mid = (left + right) // 2
        if i == A[mid]:
            isExist = True
            arr.append(1)
            break
        elif i < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if not isExist:
        arr.append(0)

print(' '.join(map(str, arr)))
