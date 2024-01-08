import sys

input_line = sys.stdin.readline

N = int(input_line())
color_paper = [list(map(int, input_line().split())) for _ in range(N)]
color_paper_result = [0, 0]

total_sum = 0
for row in color_paper:
    total_sum += sum(row)


# 0 white 1 blue
def find_color_paper(x, y, size, color):
    if size == 1:
        return

    offset = size // 2

    check_paper = [[], [], [], []]
    for col in color_paper[y:y + offset]:
        for row in col[x:x + offset]:
            check_paper[0].append(row)
        for row in col[x + offset:x + size]:
            check_paper[1].append(row)

    for col in color_paper[y + offset:y + size]:
        for row in col[x:x + offset]:
            check_paper[2].append(row)
        for row in col[x + offset:x + size]:
            check_paper[3].append(row)



    for idx in range(len(check_paper)):
        if sum(check_paper[idx]) != offset * offset * color:
            dx, dy = x, y
            if idx == 1:
                dx += offset
            elif idx == 2:
                dy += offset
            elif idx == 3:
                dx += offset
                dy += offset
            find_color_paper(dx, dy, offset, color)
        else:
            color_paper_result[color] += 1


if total_sum == 0:
    print(1)
    print(0)
elif total_sum == N * N:
    print(0)
    print(1)
else:
    find_color_paper(0, 0, N, 1)
    find_color_paper(0, 0, N, 0)
    print(color_paper_result[0])
    print(color_paper_result[1])
