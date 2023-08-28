import sys

input = sys.stdin.readline


def solution(num):
    ans_m = '7' * (num % 2) + '1' * (num // 2 - (num % 2))

    ans = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    if num <= 10:
        ans_n = ans[num]
    else:
        ans_n = ''
        while num > 0:
            num -= 7
            if num >= 0:
                ans_n += '8'
            else:
                num += 7
                break
        small = {2: '1', 5: '2', 6: '6'}
        if num in small:
            ans_n = small[num] + ans_n
        else:
            if num == 1:
                ans_n = '10' + ans_n[1:]
            elif num == 3:
                ans_n = '200' + ans_n[2:]
            elif num == 4:
                ans_n = '20' + ans_n[1:]
    print(ans_n, end=" ")
    print(ans_m)


t = int(input())
for _ in range(t):
    n = int(input())
    solution(n)
