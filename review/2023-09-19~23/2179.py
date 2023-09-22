import sys

input = sys.stdin.readline
n = int(input())
arr = [input().strip() for _ in range(n)]

arr1 = sorted(list(enumerate(arr)), key=lambda x: x[1])


def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt


length = [0] * (n + 1)
for i in range(n - 1):
    tmp = check(arr1[i][1], arr1[i + 1][1])
    length[arr1[i][0]] = max(length[arr1[i][0]], tmp)
    length[arr1[i + 1][0]] = max(length[arr1[i + 1][0]], tmp)

first = 0
for i in range(n):
    if first == 0:
        if length[i] == max(length):
            first = arr[i]
            print(first)
            pre = arr[i][:max(length)]
    else:
        if max(length) == length[i] and pre == arr[i][:max(length)]:
            print(arr[i])
            exit()