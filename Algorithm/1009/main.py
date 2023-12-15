import sys

input_line = sys.stdin.readline

T = int(input_line())

for _ in range(T):
    a, b = map(int, input_line().split())
    temp = a % 10
    # a의 거듭제곱 형식이기 때문에 마지막 자리의 거듭제곱 패턴
    # 사실 시간초과가 문제다
    if temp == 0:
        print(10)
    elif temp in [1, 5, 6]:
        print(temp)
    elif temp in [4, 9]:
        # 2가지 케이스가 나오려면 거듭제곱이 2가지 패턴 즉 나머지가 0, 1
        case = b % 2
        print(temp ** 2 % 10 if case == 0 else temp ** 1 % 10)
    else:
        # 4가지 케이스가 나오려면 거듭제곱이 4가지 0, 1, 2, 3
        case = b % 4
        print(temp ** 4 % 10 if case == 0 else temp ** case % 10)
