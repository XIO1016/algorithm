import sys

input = sys.stdin.readline


def check_game_end(case, t):
    if case[0] == t and case[0] == case[1] == case[2]:
        return True
    elif case[0] == t and case[0] == case[3] == case[6]:
        return True
    elif case[4] == t and case[1] == case[4] == case[7]:
        return True
    elif case[4] == t and case[3] == case[4] == case[5]:
        return True
    elif case[8] == t and case[6] == case[7] == case[8]:
        return True
    elif case[8] == t and case[2] == case[5] == case[8]:
        return True
    elif case[4] == t and case[0] == case[4] == case[8]:
        return True
    elif case[4] == t and case[2] == case[4] == case[6]:
        return True
    else:
        return False


while True:
    a = input().strip()
    if a == "end":
        break
    x_cnt = a.count('X')
    o_cnt = a.count('O')

    if x_cnt == o_cnt + 1 or x_cnt == o_cnt:
        if x_cnt == o_cnt + 1:
            t1, t2 = 'X', 'O'
        else:
            t1, t2 = 'O', 'X'
        result1 = check_game_end(a, t1)
        result2 = check_game_end(a, t2)

        if result2:
            print("invalid")
        elif not result1:
            if a.count('.') == 0:
                print("valid")
            else:
                print("invalid")
        else:
            print("valid")
    else:
        print("invalid")
