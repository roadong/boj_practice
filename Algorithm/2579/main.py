import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N = int(input())

stairs = [int(input()) for _ in range(N)]
sum_stair = [[0, 0, 0] for _ in range(N)]


def step_stair(idx, continue_cnt):
    if idx == N - 1:
        return stairs[N - 1]

    target_stair = sum_stair[idx][continue_cnt]
    if target_stair != 0:
        return target_stair

    sum_max = 0
    if continue_cnt != 2:
        temp = step_stair(idx + 1, continue_cnt + 1) + stairs[idx]
        sum_max = sum_max if sum_max > temp else temp

    if idx < N - 2:
        temp = step_stair(idx + 2, 1) + stairs[idx]
        sum_max = sum_max if sum_max > temp else temp

    # target_stair = sum_max
    return sum_max


max_sum = 0
temp = step_stair(0, 1)
max_sum = max_sum if max_sum > temp else temp
temp = step_stair(1, 1)
max_sum = max_sum if max_sum > temp else temp

print(max_sum)



