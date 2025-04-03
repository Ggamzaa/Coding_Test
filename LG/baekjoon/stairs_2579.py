import sys

input = sys.stdin.readline

n = int(input())
list = [int(input()) for _ in range(n)]

for item in list:
    print(item)