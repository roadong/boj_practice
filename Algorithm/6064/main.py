import sys

input_line = sys.stdin.readline

T = int(input_line())

# 10 12 3 9
# 10 12 7 2
# 13 11 5 6
for _ in range(T):
    # M : x의 최대, N: y의 최대
    M, N, x, y = map(int, input_line().split())
    k = 0
    n = 0
    result = -1
    while k <= M * N:
        k = n * M + x
        if (k - x) % M == 0 and (k - y) % N == 0:
            result = k
            break
        else:
            n += 1

    print(result)
