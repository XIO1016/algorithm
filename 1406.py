import sys

input = sys.stdin.readline
string = list(input().strip())
m = int(input())
string2 = []
for _ in range(m):
    i = input().split()
    cmd = i[0]
    if cmd == "L":
        if string:
            string2.append(string.pop())
    elif cmd == "D":
        if string2:
            string.append(string2.pop())
    elif cmd == "B":
        if string:
            string.pop()
    elif cmd == "P":
        string.append(i[1])
print("".join(string + list(reversed(string2))))
