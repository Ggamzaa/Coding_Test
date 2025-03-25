import sys

input = sys.stdin.readline

n = int(input())

result = -1

for i in range(n // 5, -1, -1):
    remain = n - (5 * i)
    if remain % 3 == 0:
        result = i + (remain // 3)
        break

print(result)