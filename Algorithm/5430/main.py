import sys
from collections import deque

input_line = sys.stdin.readline
# R -> reverse, D -> first element drop
# 단순 구현이 아니라 퍼포먼스도 신경써야한다 (리스트 뒤집을 필요없이 꺼내는 방법을 달리)
T = int(input_line())

for _ in range(T):
    is_error = False
    P = input_line().rstrip()
    N = int(input_line())
    num_list = deque(list(input_line().rstrip()[1:-1].split(',')))
    is_reverse = False
    for command in list(P):
        if command == 'R':
            is_reverse = not is_reverse
        else:
            if len(num_list) == 0 or num_list[0] == '':
                is_error = True
                break
            if is_reverse:
                num_list.pop()
            else:
                num_list.popleft()

    if not is_error:
        if is_reverse:
            num_list.reverse()
        print(f'[{",".join(num_list)}]')
    else:
        print('error')

