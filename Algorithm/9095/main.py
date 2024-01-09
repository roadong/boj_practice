import sys

input_line = sys.stdin.readline

T = int(input_line())
calc = [0] * 11

calc[1] = 1
calc[2] = 2
calc[3] = 4

for i in range(4, 11):
    calc[i] = calc[i-1] + calc[i-2] + calc[i-3]

for _ in range(T):
    N = int(input_line())

    print(calc[N])

