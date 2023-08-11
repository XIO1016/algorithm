import sys

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        l = [int(input()) for _ in range(n)]
        ans = []
        l.sort()
        left, right = 0, n - 1
        while left < right:
            if l[left] + l[right] < x:
                left += 1
            elif l[left] + l[right] > x:
                right -= 1
            else:
                ans = [l[left], l[right]]
                break
        if ans:
            print('yes {0} {1}'.format(ans[0], ans[1]))
        else:
            print('danger')

    except:
        break
