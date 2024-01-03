import sys

input_line = sys.stdin.readline

# 0 1 3
T = int(input_line())

result = [0, 0]
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0

dp[1][0] = 0
dp[1][1] = 1

dp[2][0] = 1
dp[2][1] = 1

dp[3][0] = dp[2][0] + dp[1][0]
dp[3][1] = dp[2][1] + dp[1][1]

for _ in range(T):
    case = int(input_line())
    if case < 3:
        print(*dp[case])
    else:
        for i in range(3, case + 1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
        print(*dp[case])