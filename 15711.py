import sys

input = sys.stdin.readline

n = 2 * (10 ** 6)
a = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if a[i]:
        a[2 * i::i] = [False] * ((n - i) // i)
prime = [i for i in range(2, n) if a[i]]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a + b < 4:
        print("NO")
    elif (a + b) % 2 == 0:
        print("YES")
    else:
        if a + b - 2 >= n:
            flag = 0
            for p in prime:
                if (a + b - 2) % p == 0:
                    flag = 1
                    print("NO")
                    break
            if not flag:
                print("YES")
        else:
            if a + b - 2 in prime:
                print("YES")
            else:
                print("NO")
