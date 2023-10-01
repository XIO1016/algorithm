import sys
from math import factorial

input = sys.stdin.readline
n, m = map(int, input().split())

print(int(factorial(n) // (factorial(n - m) * factorial(m))))
