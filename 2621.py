import sys

input = sys.stdin.readline

card = [list(input().split()) for _ in range(5)]

color = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
num = [0] * 11

card_num = [int(x[1]) for x in card]
for i in range(5):
    color[card[i][0]] += 1
    num[int(card[i][1])] += 1
score = 0

sort_nums = card_num.copy()
sort_nums.sort()

if 5 in color.values() and sort_nums[0] + 1 == sort_nums[1] and sort_nums[1] + 1 == sort_nums[2] and sort_nums[2] + 1 == \
        sort_nums[3] and sort_nums[3] + 1 == sort_nums[4]:
    score = max(card_num) + 900

elif 4 in num:
    score = num.index(4) + 800

elif 3 in num and 2 in num:
    score = num.index(3) * 10 + num.index(2) + 700

elif 5 in color.values():
    score = max(card_num) + 600

elif sort_nums[0] + 1 == sort_nums[1] and sort_nums[1] + 1 == sort_nums[2] and sort_nums[2] + 1 == sort_nums[3] and \
        sort_nums[3] + 1 == sort_nums[4]:
    score = max(card_num) + 500
elif 3 in num:
    score = num.index(3) + 400
elif 2 in num:
    first = num.index(2)
    num1 = card_num.copy()
    for i in num1:
        if i == first:
            card_num.remove(i)
    num[first] = 0
    if 2 in num:
        second = num.index(2)
        score = max(first, second) * 10 + min(first, second) + 300
    else:
        score = first + 200
else:
    score = max(card_num) + 100
print(score)
