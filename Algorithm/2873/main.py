import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)
r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]


def greedy_sol():
    move: str = ''
    if not r % 2 and not c % 2:
        index = find_lower_point()
        front_cnt = index[0] // 2
        tail_cnt = (r // 2) - 1 - front_cnt
        move += ('R'*(c-1)+'D'+'L'*(c-1)+'D') * front_cnt
        move += 'DRUR' * (index[1] // 2)
        move += 'DR' if index[1] % 2 else 'RD'
        move += 'RURD' * (c // 2 - 1 - (index[1] // 2))
        move += ('D' + 'L'*(c-1) + 'D' + 'R'*(c-1)) * tail_cnt
    else:
        if r % 2:
            move += ('R'*(c-1)+'D'+'L'*(c-1)+'D')*(r//2)+('R'*(c-1))
        else:
            move += ('D'*(r-1)+'R'+'U'*(r-1)+'R')*(c//2)+('D'*(r-1))

    return move


def find_lower_point():
    min_val = 1001
    index = []
    for cur_r in range(r):
        for cur_c in range(c):
            if (cur_c + cur_r) % 2:
                if min_val > arr[cur_r][cur_c]:
                    min_val = arr[cur_r][cur_c]
                    index = [int(cur_r), int(cur_c)]
    return index


print(greedy_sol())
