import sys

input_line = sys.stdin.readline

T = int(input_line())

for _ in range(T):
    closet = dict()
    result = 1
    N = int(input_line())
    for _ in range(N):
        wear, category = input_line().rstrip().split(' ')
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1

    for value in closet.values():
        # 조합 수 = (각 카테고리에서 옷을 입는 숫자 + 카테고리에서 의상을 안 입을 경우)
        result *= (value + 1)

    # 모두 안 입을 경우의 수를 하나 빼준다
    print(result - 1)


