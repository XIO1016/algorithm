n = int(input())

arr = list(map(int, input().split()))

left, right = 0, n - 1
a, b = 0, n - 1
ans = float("inf")
while left < right:
    tmp = arr[left] + arr[right]
    if ans > abs(tmp):
        ans = abs(tmp)
        a, b = arr[left], arr[right]
    if tmp == 0:
        break
    elif tmp < 0:
        left += 1
    else:
        right -= 1
print(a, b)
