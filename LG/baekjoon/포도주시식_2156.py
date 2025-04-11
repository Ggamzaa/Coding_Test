import sys

input = sys.stdin.readline

n = int(input())
glass = [int(input()) for _ in range(n)]

if n == 1:
    print(glass[0])
elif n == 2:
    print(glass[0] + glass[1])
else:
    dp = [0] * n
    dp[0] = glass[0]
    dp[1] = glass[0] + glass[1]
    dp[2] = max(glass[0] + glass[2], glass[1] + glass[2])
    # dp[2] = max(glass[0] + glass[1], dp[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2] + glass[i], dp[i-3] + glass[i-1] + glass[i])

    print(dp[-1])