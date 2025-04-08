import sys

input = sys.stdin.readline

n = int(input())
list = [int(input()) for _ in range(n)]

# for item in list:
#     print(item)

'''
1. 1칸 아니면 2칸씩 올라갈 수 있음
2. 연속으로 세칸은 못 올라감
3. 마지막칸은 무조건 지나야함
'''

