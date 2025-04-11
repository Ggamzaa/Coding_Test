import sys

input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]

# for item in list:
#     print(item)

'''
1. 1칸 아니면 2칸씩 올라갈 수 있음
2. 연속으로 세칸은 못 올라감
3. 마지막칸은 무조건 지나야함
'''

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0] + stair[1])
else:
    dp = [0] * n
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

    print(dp[-1])