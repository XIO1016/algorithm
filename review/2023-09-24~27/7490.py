import copy


def recursive(arr, m):
    if len(arr) == m:
        operator.append(copy.deepcopy(arr))
        return
    arr.append('+')
    recursive(arr, m)
    arr.pop()

    arr.append(' ')
    recursive(arr, m)
    arr.pop()

    arr.append('-')
    recursive(arr, m)
    arr.pop()


for _ in range(int(input())):
    n = int(input())
    operator = []
    recursive([], n - 1)
    for o in operator:
        s = ''
        for i in range(n - 1):
            s += str(i + 1) + o[i]
        s += str(n)
        if eval(s.replace(' ', '')) == 0:
            print(s)
