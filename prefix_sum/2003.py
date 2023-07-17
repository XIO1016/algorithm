import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
left = 0
right = 1
result = 0

while n >= right >= left:
    sum_num = lst[left:right]
    total = sum(sum_num)
    if total == m:
        result += 1
        right += 1
    elif total > m:
        left += 1
    else:
        right += 1
print(result)
