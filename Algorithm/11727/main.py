from sys import stdin

input_line = stdin.readline

N = int(input_line())

divide_const = 10007

# 점화식 유도
dp = [0, 1, 3, 5]
# 2x2 경우 수가 추가 되는 경우는
# dp2 = [0, 0, 1, 2, 3, 5]
# dp2[4] -> dp[2]
# dp[4] = dp[3] + dp[2] + dp[2]
# dp[5] = dp[4] + dp[3] + dp[3]

if N > 3:
    for i in range(4, 1001):
        # dp2.append(dp2[i - 1] + 2 dp2[i - 2])
        dp.append((dp[i - 1] + (2 * dp[i - 2])) % 10007)


print(dp[N])

