import sys

input_line = sys.stdin.readline

N, r, c = map(int, input_line().split())
result = 2 ** (N * 2) - 1
size = 2 ** N


def div_con(x, y):
    global size, result
    if size == 1:
        return result
    else:
        offset = size // 2
        next_x = x % offset
        next_y = y % offset
        # 3 or 4 분면
        if offset <= x:
            # 3
            if offset > y:
                result -= (offset ** 2) * 1
        # 1 or 2분면
        else:
            # 1분면
            if offset > y:
                result -= (offset ** 2) * 3
            # 2분면
            else:
                result -= (offset ** 2) * 2

        size /= 2
        div_con(next_x, next_y)


div_con(r, c)
print(int(result))
