import sys

input_line = sys.stdin.readline

T = int(input_line())
# 점화식 유도
# P[1] = 1
# P[2] = 1
# P[3] = 1
# P[4] = 2
# P[5] = 2
# P[6] = P[5] + P[1] 3
# P[7] = P[6] + P[2] 4
# P[8] = P[7] + P[3] 5
# P[9] = P[8] + P[4] 7
# P[10] = P[9] + P[5] 9
# P[11] = P[10] + P[6] 12
# P[12] = P[11] + P[7] 16
# P[13] = P[12] + P[8]
# P[14] = P[13] + P[9]
# P[15] = P[14] + P[10]
# 사전 입력
result = [0, 1, 1, 1, 2, 2]

for idx in range(6, 101):
    result.append(result[idx - 1] + result[idx - 5])

for _ in range(T):
    N = int(input_line())

    print(result[N])
