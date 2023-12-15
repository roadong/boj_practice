import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N = int(input())

meets_list = []
for _ in range(N):
    meets_list.append(tuple(map(int, input().split())))

meets_list.sort(key=lambda x: (x[1], x[0]))

cnt = 1
# 첫 비교 변수
pre_end = meets_list[0][1]
for i in range(1, N):
    if meets_list[i][0] >= pre_end:
        cnt += 1
        pre_end = meets_list[i][1]


print(cnt)



