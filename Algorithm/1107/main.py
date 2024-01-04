import sys

input_line = sys.stdin.readline

N = int(input_line())

# 고장난 버튼 갯수
M = int(input_line())
target = list(str(N))
cur_ch = 100
break_buttons = []
if M > 0:
    break_buttons = input_line().rstrip().split()

buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

cnt = 0
# case N을 중심으로 가까운 큰 수, 작은 수 중에 적은 차이가 나는게 가까운 것
min_distance = abs(cur_ch - N)

if cur_ch == N:
    print(0)
else:
    for i in range(1_000_000):

        is_correct = True
        for c in list(str(i)):
            if c in break_buttons:
                is_correct = False

        if not is_correct:
            continue

        diff = len(str(i)) + abs(i - N)
        if diff < min_distance:
            min_distance = diff

    print(min_distance)
