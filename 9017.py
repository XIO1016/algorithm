import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    score = list(map(int, input().split()))
    count = {}
    for i in range(n):
        try:
            count[score[i]] += 1
        except:
            count[score[i]] = 1
    dele = {}
    for k, v in count.items():
        if v < 6:
            dele[k] = 1

    team = {}
    idx = 1
    for i in range(n):
        if score[i] not in dele:
            try:
                if team[score[i]][0] < 4:
                    team[score[i]][0] += 1
                    team[score[i]][1] += idx
                elif team[score[i]][0] == 4:
                    team[score[i]][0] += 1
                    team[score[i]][2] = idx
            except:
                team[score[i]] = [1, idx, 0]
            idx += 1
    team = sorted(team.items(), key=lambda x: (x[1][1], x[1][2]))
    print(team[0][0])
