import sys
from collections import deque

input_line = sys.stdin.readline

N = int(input_line())

dp = [sys.maxsize] * (N + 1)


def calc_one(n):
    d_queue = deque([n])
    dp[n] = 0
    while d_queue:
        next_x = d_queue.popleft()

        if next_x == 1:
            break

        # 3 나누기
        if next_x % 3 == 0:
            d_queue.append(next_x // 3)
            dp[next_x // 3] = min(dp[next_x] + 1, dp[next_x // 3])

        # 2 나누기
        if next_x % 2 == 0:
            d_queue.append(next_x // 2)
            dp[next_x // 2] = min(dp[next_x] + 1, dp[next_x // 2])
        
        # 1 빼기
        d_queue.append(next_x - 1)
        dp[next_x - 1] = min(dp[next_x] + 1, dp[next_x - 1])


calc_one(N)
print(dp[1])
