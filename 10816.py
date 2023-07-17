import sys

input = sys.stdin.readline
n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))
lst = []
count = {}
for a in A:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1


def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


for target in B:
    print(binary_search(A, target, 0, n - 1), end=" ")
