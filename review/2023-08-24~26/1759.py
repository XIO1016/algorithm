import sys

input = sys.stdin.readline

l, c = map(int, input().split())
arr = list(input().strip().split())

ans = []


def recursive(cnt, idx):
    if cnt == l:
        cnt1, cnt2 = 0, 0
        for a in ans:
            if a in ['a', 'e', 'i', 'o', 'u']:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            print(''.join(ans))
        return
    for i in range(idx, l):
        ans.append(arr[i])
        recursive(cnt + 1, idx + 1)
        ans.pop()
