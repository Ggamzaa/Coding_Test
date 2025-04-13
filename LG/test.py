import sys

input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

#초기값 설정
if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:
    dp = [0] * n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

    # 초기값 이외의 계산
    for i in range(3, n):
        dp[i] = max(
            dp[i-1],
            dp[i-2] + wine[i],
            dp[i-3] + wine[i-1] + wine[i]
        )

    print(dp[-1])