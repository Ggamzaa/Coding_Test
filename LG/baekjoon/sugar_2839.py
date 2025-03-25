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


# dp = [1e9] * (n + 1)  # 충분히 큰 값으로 초기화
# dp[0] = 0  # 0kg은 0개 필요

# for i in range(3, n + 1):
#     if i >= 3:
#         dp[i] = min(dp[i], dp[i - 3] + 1)
#     if i >= 5:
#         dp[i] = min(dp[i], dp[i - 5] + 1)

# print(dp[n] if dp[n] != 1e9 else -1)