import sys
from sys import stdin

input_line = stdin.readline


N = int(input_line().rstrip())
dp = [sys.maxsize] * 50001
dp[0], dp[1] = 0, 1

for i in range(1, N + 1):

    j = 1
    while j ** 2 <= i:
        # 해당 조합으로 만들 수 있는 것에 최소값을 갱신
        # 조합을 찾아나가는 과정은 현재 숫자를 더 작은 제곱 수로 만든 조합 수 중 최소값
        # 4는 다음 2의 제곱과 1의 제곱의 조합 수로 나타낼 수 있다
        dp[i] = min(dp[i], dp[i - (j ** 2)])
        j += 1

    dp[i] += 1


print(dp[N])