import sys

input_line = sys.stdin.readline

# s : 시간
# N : 가장 작은 단위의 사각형
# K : 가운데 K 크기로 사각형이 채워지는 숫자
# (R1, C1), (R2, C2) : 시간이 s일때 출력할 좌표
s, N, K, R1, R2, C1, C2 = map(int, input_line().split())
# 1 5 3 0 4 0 4
# 2 3 1 0 8 0 8
# 3 3 1 4 11 5 10
# 2 8 4 56 61 33 56

# 전체 프랙탈 사이즈
fractal_size = N ** s
# 가운데 검게 칠할 첫 인덱스
fill_square_start = (N - K) // 2
fill_square_end = (N + K) // 2


# 해당 프랙탈 스퀘어의 칠할 부분을 리턴
def fill_point(size, u, v):
    # 사이즈가 1이면 0 리턴
    if size == 1:
        return 0

    next_search_size = size // N
    # 해당 좌표가 가운데 검은색을 칠하는 위치면 1 리턴
    if (next_search_size * fill_square_start <= u < next_search_size * fill_square_end
            and next_search_size * fill_square_start <= v < next_search_size * fill_square_end):
        return 1

    # 다음 찾을 사이즈 (Top - Down)
    return fill_point(next_search_size, u % next_search_size, v % next_search_size)


for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        print(fill_point(fractal_size, i, j), end='')
    print()
