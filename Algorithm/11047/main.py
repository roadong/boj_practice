import sys

input_line = sys.stdin.readline

N, K = map(int, input_line().split())

currency_grade = [int(input_line()) for _ in range(N)]

# N번 째 수는 N - 1번째의 배수
currency_grade.reverse()
cnt = 0
for current in currency_grade:
    if K >= current:
        cnt += K // current
        K %= current
        if K == 0:
            break

print(cnt)

