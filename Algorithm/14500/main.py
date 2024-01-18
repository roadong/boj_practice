from sys import stdin

input_line = stdin.readline

# N: 세로, M: 가로
N, M = map(int, input_line().rstrip().split())
tetris_map = [list(map(int, input_line().rstrip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
move_mask = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_res = 0


# 4개를 탐색하고 최대값 갱신
def dfs(u, v, cur_block_cnt, cur_tetromino_sum):
    global max_res

    # 4개를 완성하면 최대값 갱신하고 리턴
    if cur_block_cnt == 4:
        max_res = max(max_res, cur_tetromino_sum)
        return

    for move_x, move_y in move_mask:
        next_x, next_y = u + move_x, v + move_y
        if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
            # 2번째 블록에서 탐색할 경우 ㅗ형은 별도 처리
            if cur_block_cnt == 2:
                visited[next_x][next_y] = True
                dfs(u, v, cur_block_cnt + 1, cur_tetromino_sum + tetris_map[next_x][next_y])
                visited[next_x][next_y] = False

            visited[next_x][next_y] = True
            dfs(next_x, next_y, cur_block_cnt + 1, cur_tetromino_sum + tetris_map[next_x][next_y])
            visited[next_x][next_y] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, tetris_map[i][j])
        visited[i][j] = False

print(max_res)
