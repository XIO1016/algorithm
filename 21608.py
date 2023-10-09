import sys

input = sys.stdin.readline

n = int(input())
students = [list(map(int, input().split())) for _ in range(n * n)]
