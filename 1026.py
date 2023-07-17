import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A2 = sorted(A)
sum = 0
for i in range(n):
    sum += A2[i] * B[B.index(max(B))]
    B.remove(max(B))
print(sum)
