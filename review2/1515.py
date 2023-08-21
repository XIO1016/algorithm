import sys

input = sys.stdin.readline

nums = input().strip()
i = 0
while True:
    i += 1
    n = str(i)
    print('n: ', n)
    while len(n) > 0 and len(nums) > 0:
        if nums[0] == n[0]:
            nums = nums[1:]
        n = n[1:]
        print('n: ', n)
    if nums == '':
        print(i)
        break
