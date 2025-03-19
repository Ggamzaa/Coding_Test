aw_input = """
        8
        7 2 1 8 4 3 5 6
        """

N = int(input().strip())
P = list(map(int, input().split()))

dp = [[float('-inf')] * 2 for _ in range(N + 1)]
dp[0][0] = 0  # 아무것도 안 먹었을 때

for i in range(1, N + 1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] - P[i-1])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] + P[i-1])

print(dp[N][1])