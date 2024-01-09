import sys

input_line = sys.stdin.readline

# I의 갯수
N = int(input_line())

# S의 길이
M = int(input_line())

S = input_line().rstrip()

cnt = 0
l, r = 0, 0
while r < M:
    # 부분 매칭 을 찾는다
    if S[r: r + 3] == 'IOI':
        # 블록 크기가 될 때 까지 커서를 늘린다
        r += 2
        # 블록 크기와 같으면 카운팅
        if r - l == 2 * N:
            cnt += 1
            # 다음 I로 이동
            l += 2

    # 아닌 경우 커서를 하나씩 이동
    else:
        r += 1
        l = r

print(cnt)
