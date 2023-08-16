import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().strip())
cnt = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and arr[j] == 'H':
                cnt += 1
                arr[j] = 'h'
                break
print(cnt)
