import sys
from collections import deque

input_line = sys.stdin.readline

M, N = map(int, input_line().split())

tomato_box = [list(map(int, list(input_line().rstrip().split(' ')))) for _ in range(N)]
move_mask = [(1, 0), (-1, 0), (0, 1), (0, -1)]
d_queue = deque()

for n in range(N):
    for m in range(M):
        if tomato_box[n][m] == 1:
            d_queue.append((n, m))

day_cnt = 0
while d_queue:
    x, y = d_queue.popleft()
    for mask_x, mask_y in move_mask:
        dx, dy = x + mask_x, y + mask_y
        if 0 <= dx < N and 0 <= dy < M:
            if tomato_box[dx][dy] == 0:
                tomato_box[dx][dy] = tomato_box[x][y] + 1
                day_cnt = max(day_cnt, tomato_box[dx][dy])
                d_queue.append((dx, dy))


def check_complete():
    for i in range(N):
        for j in range(M):
            if tomato_box[i][j] == 0:
                return False

    return True


if not check_complete():
    print(-1)
else:
    if day_cnt == 0:
        print(0)
    else:
        print(day_cnt - 1)
