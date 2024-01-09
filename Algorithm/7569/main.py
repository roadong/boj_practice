import sys
from collections import deque

input_line = sys.stdin.readline


# M : 가로, N: 세로, H: 높이
# Bfs + 경로 누적
M, N, H = map(int, input_line().split())
queue_list = []
tomato_box = [[list(map(int, list(input_line().rstrip().split(' ')))) for _ in range(N)] for _ in range(H)]
move_mask = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
d_queue = deque()
is_already_complete = True
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato_box[h][n][m] == 1:
                d_queue.append((h, n, m))
            elif tomato_box[h][n][m] == 0:
                is_already_complete = False


day = 0
# -1 : 토마토 없음 0: 덜익은 토마토 1: 익은 토마토
while d_queue:
    h, n, m = d_queue.popleft()
    for mask_n, mask_m, mask_h in move_mask:
        dn, dm, dh = n + mask_n, m + mask_m, h + mask_h
        if 0 <= dn < N and 0 <= dm < M and 0 <= dh < H:
            if tomato_box[dh][dn][dm] == 0:
                tomato_box[dh][dn][dm] = tomato_box[h][n][m] + 1
                day = max(day, tomato_box[dh][dn][dm])
                d_queue.append((dh, dn, dm))

is_complete = True
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato_box[h][n][m] == 0:
                is_complete = False
                break
        if not is_complete:
            break
    if not is_complete:
        break

if not is_complete:
    print(-1)
else:
    if day == 0:
        print(0)
    else:
        print(day - 1)
