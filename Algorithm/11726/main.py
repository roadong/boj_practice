from sys import stdin

input_line = stdin.readline

N = int(input_line())

divide_const = 10007

# 2x1 1x2 로 채우는 방법의 수를 10007로 나눈 나머지
dp = [0, 1, 2]

# dp[3] = 3 -> dp[1] + dp[2]
# dp[4] = 5 -> dp[2] + dp[3]

for i in range(3, 1001):
    dp.append((dp[i - 1] + dp[i - 2]) % 10007)

print(dp[N])