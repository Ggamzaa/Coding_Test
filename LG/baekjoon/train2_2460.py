import sys

input = sys.stdin.readline

n = 10
people = [tuple(map(int, input().split())) for _ in range(int(n))]
max = 0
cnt = 0

for o,i in people:
    cnt -= o 
    cnt += i
    if cnt > max:
        max = cnt

print(max)
    