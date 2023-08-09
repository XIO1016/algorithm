import sys

input = sys.stdin.readline

l, c = map(int, input().split())
arr = list(input().strip().split())
arr.sort()
a = ['a', 'e', 'i', 'o', 'u']

answer = []


def back_tracking(cnt, idx):
    if cnt == l:
        cnt1, cnt2 = 0, 0
        for i in range(l):
            if answer[i] in a:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            print("".join(answer))
        return
    for i in range(idx, c):
        answer.append(arr[i])
        back_tracking(cnt + 1, i + 1)
        answer.pop()


back_tracking(0, 0)
