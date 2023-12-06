import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N = int(input())

stairs = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
elif N == 3:
    print(max(stairs[0], stairs[1]) + stairs[2])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[1] + stairs[0]
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]

    for idx in range(3, N):
        dp_sol_one_step = stairs[idx - 1] + stairs[idx] + dp[idx - 3]
        dp_sol_two_step = stairs[idx] + dp[idx - 2]
        dp[idx] = max(dp_sol_one_step, dp_sol_two_step)

    print(dp[N - 1])

